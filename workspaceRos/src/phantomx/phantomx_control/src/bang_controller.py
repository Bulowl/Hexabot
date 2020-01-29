#!/usr/bin/env python

import rospy
import rospkg
import numpy as np

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def follow_wall(lidar_scan):
    min_range, max_range = 0,len(lidar_scan.ranges)-1
    
    d_right_list, d_left_list = lidar_scan.ranges[min_range:min_range+100], lidar_scan.ranges[max_range-100:max_range]
    d_left, d_right = np.median(d_left_list)<1, np.median(d_right_list)<1
    
    cmd_vel_msg.angular.z = - 0.6*d_left + 0.6*d_left
    cmd.publish(cmd_vel_msg)


if __name__ == '__main__':
    rospy.init_node("bang_controller")

    rospy.loginfo('Cave Exploration Starting')

    cmd_vel_msg = Twist()

    cmd_vel_msg.linear.x = 0.4

    rospy.sleep(1)
    cmd = rospy.Publisher("/phantomx/cmd_vel",Twist, queue_size=5)
    lidar_scan = rospy.Subscriber("/phantomx/scan", LaserScan, follow_wall)


    while not rospy.is_shutdown():
        rospy.sleep(1)

    rospy.loginfo('Cave Exploration Finished')
