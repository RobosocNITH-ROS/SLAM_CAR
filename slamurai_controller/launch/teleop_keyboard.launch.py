import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # teleop_twist_keyboard node
    teleop_twist_keyboard = Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            name='teleop_twist_keyboard',
            
            prefix='gnome-terminal --',  # Launch in gnome-terminal
            output='screen',
        )

    # twist_to_twist_stamped node
    twist_to_twist_stamped = Node(
        package="slamurai_controller",
        executable="twist_to_twiststamped.py",
        name="twist_to_twiststamped",
        output="screen",
    )

    return LaunchDescription(
        [
            teleop_twist_keyboard,
            twist_to_twist_stamped
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


