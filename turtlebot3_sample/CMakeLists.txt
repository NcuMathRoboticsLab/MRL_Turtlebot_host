cmake_minimum_required(VERSION 2.8.3)
project(turtlebot3_sample)

find_package(catkin REQUIRED
	roscpp
	std_msgs
	sensor_msgs
	diagnostic_msgs
	turtlebot3_msgs
)

catkin_package(CATKIN_DEPENDS roscpp std_msgs sensor_msgs diagnostic_msgs turtlebot3_msgs)

include_directories(
	${catkin_INCLUDE_DIRS}
)

add_executable(sample src/sample.cpp)
target_link_libraries(sample ${catkin_LIBRARIES})