import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    use_slam = LaunchConfiguration("use_slam")

    use_slam_arg = DeclareLaunchArgument(
        "use_slam",
        default_value="false"
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("slamurai_description"),
                "launch",
                "gazebo.launch.py"
            )
        ),
        launch_arguments={
            "world_name": "custom_world"
        }.items()
    )
    controller = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slamurai_controller"),
            "launch",
            "controller.launch.py"
        ),
       
    )
    
    # joystick = IncludeLaunchDescription(
    #     os.path.join(
    #         get_package_share_directory("slamurai_controller"),
    #         "launch",
    #         "joystick_teleop.launch.py"
    #     ),
    #     launch_arguments={
    #         "use_sim_time": "True"
    #     }.items()
    # )

    teleop = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slamurai_controller"),
            "launch",
            "teleop_keyboard.launch.py"
        ),
        launch_arguments={
            "use_sim_time": "True"
        }.items()
    )



    localization = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slamurai_localization"),
            "launch",
            "global_localization.launch.py"
        ),
        condition=UnlessCondition(use_slam)
    )

    local_localization = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slamurai_localization"),
            "launch",
            "local_localization.launch.py"
        ),
        condition=IfCondition(use_slam)
    )


    slam = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slamurai_mapping"),
            "launch",
            "slam.launch.py"
        ),
        condition=IfCondition(use_slam)
    )

    rviz_localization = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", os.path.join(
                get_package_share_directory("slamurai_localization"),
                "rviz",
                "global_localization.rviz"
            )
        ],
        output="screen",
        parameters=[{"use_sim_time": True}],
        condition=UnlessCondition(use_slam)
    )

    rviz_slam = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", os.path.join(
                get_package_share_directory("slamurai_mapping"),
                "rviz",
                "slam.rviz"
            )
        ],
        output="screen",
        parameters=[{"use_sim_time": True}],
        condition=IfCondition(use_slam)
    )
    
    return LaunchDescription([
        use_slam_arg,
        local_localization,
        gazebo,
        controller,
        teleop,
        localization,
        slam,
        rviz_localization,
        rviz_slam
    ])
