cmake_minimum_required(VERSION 3.0.2)
project(turtlebot3_py_sample)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
  diagnostic_msgs
  turtlebot3_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs sensor_msgs diagnostic_msgs turtlebot3_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/sample.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

