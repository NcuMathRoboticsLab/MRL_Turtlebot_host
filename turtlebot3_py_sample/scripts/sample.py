import rospy
import math
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

counter = 0

def RAD2DEG(r):
    return r * 180 / math.pi

def callback(event):
    counter += 1
    rospy.loginfo("sample file called : %d\t times, data: ", counter, event.current_real)
    
def scanCallback(scan):
    for i in range(360):
        degree = RAD2DEG(scan.angle_min + scan.angle_increment * i)
        if scan.ranges[i] > 0.001:
            print("[LIDAR INFO]:angle-distance:[%4.1f, %5.3f]", i, scan.ranges[i])

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
