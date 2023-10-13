import rospy
import math
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

counter = 0

def RAD2DEG(r):
    return r * 180 / math.pi

def callback(event):
    global counter
    
    counter += 1
    rospy.loginfo("sample file called : %d times", counter)
    
def scanCallback(scan):
    for i in range(360):
        degree = RAD2DEG(scan.angle_min + scan.angle_increment * i)
        if scan.ranges[i] > 0.001:
            print("[LIDAR INFO]:angle-distance:[{:>4.1f}, {:>5.3f}]".format(i, scan.ranges[i]))

def listener():

    rospy.init_node('listener')
    
    timer1 = rospy.Timer(rospy.Duration(0.1), callback)
    
    sub = rospy.Subscriber("/scan", LaserScan, scanCallback)

    rospy.spin()

if __name__ == '__main__':
    listener()
