import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Declare the 'use_sim_time' launch argument
    use_sim_time_arg = DeclareLaunchArgument(
        name="use_sim_time",
        default_value="True",
        description="Use simulated time"
    )

    # teleop_twist_keyboard node
    teleop_twist_keyboard = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard',
        prefix='gnome-terminal --',  # Launch in gnome-terminal
        output='screen',
        condition=IfCondition(LaunchConfiguration("use_sim_time")),
    )

    # twist_to_twist_stamped node
    twist_to_twist_stamped = Node(
        package="slamurai_controller",
        executable="twist_to_twiststamped.py",
        name="twist_to_twiststamped",
        output="screen",
        condition=IfCondition(LaunchConfiguration("use_sim_time")),
    )

    return LaunchDescription(
        [
            use_sim_time_arg,
            teleop_twist_keyboard,
            twist_to_twist_stamped,
        ]
    )


# import os
# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():

#     ld=LaunchDescription()

#     teleop_twist_keyboard = Node(
#          package="teleop_twist_keyboard",
#          executable="teleop_twist_keyboard",
#          name="teleop_twist_keyboard",
#          prefix="xterm -e",
#          )
    
#     ld.add_action(teleop_twist_keyboard)
#     return ld



# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     teleop_node = Node(
#         package='teleop_twist_keyboard',
#         executable='teleop_twist_keyboard',
        
#          prefix="xterm -e",
#         output='screen'
#     )

#     return LaunchDescription([
#         teleop_node,
#     ])


