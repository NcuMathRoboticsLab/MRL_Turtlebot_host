# MRL_Turtlebot_host

## Build  

Hosts(本機端/虛擬機端):  
```
mkdir catkin_ws && cd catkin_ws
mkdir src && cd src
git clone https://github.com/NcuMathRoboticsLab/MRL_Turtlebot_host.git .
cd ..
catkin_make
```

## How to use?

1. at hosts: `roscore` (在本機端下 `roscore`)
2. at robot: `roslaunch turtlebot3_bringup turtlebot3_robot.launch`  
  (在機器人端下 `roslaunch turtlebot3_bringup turtlebot3_robot.launch`)
3. at hosts: `rosrun turtlebot3_sample sample` or `rosrun turtlebot3_py_sample sample.py`  
  (在本機端下 `rosrun turtlebot3_sample sample` or `rosrun turtlebot3_py_sample sample.py`)

## Demo

Demo Video: https://www.youtube.com/watch?v=sj0ARlou-7A

祝大家作業順利
