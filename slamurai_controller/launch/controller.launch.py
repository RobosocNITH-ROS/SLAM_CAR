import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, GroupAction, OpaqueFunction
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():


    
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
    )

    wheel_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["slamurai_controller", 
                   "--controller-manager", 
                   "/controller_manager"
        ],
        
    )


    
    return LaunchDescription(
        [
            joint_state_broadcaster_spawner,
            wheel_controller_spawner,
            
        ]
    )
