cmake_minimum_required(VERSION 3.5)
project(slamurai_controller)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2 REQUIRED)

ament_python_install_package(${PROJECT_NAME})

# Install the launch and configuration directories
install(
  DIRECTORY launch confi
  DESTINATION share/${PROJECT_NAME}
)

# Install the Python scripts
install(PROGRAMS

  ${PROJECT_NAME}/twist_to_twiststamped.py 
  ${PROJECT_NAME}/teleop_custom.py  
  
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
