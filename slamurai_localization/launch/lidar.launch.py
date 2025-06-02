import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    

    laser_driver = Node(
    package="rplidar_ros",
    executable="rplidar_composition",  # Some ROS 2 versions use this instead of rplidar_node
    name="rplidar_node",
    parameters=[os.path.join(
        get_package_share_directory("slamurai_localization"),
        "config",
        "rplidar_a1.yaml"
    )],
    output="screen"
)
 
    
   
    
    return LaunchDescription([
      
        laser_driver,
       
    ])