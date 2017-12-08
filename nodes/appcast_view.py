#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    print '\n!'.join(data.data.split('!'))
    print
    
def listener():
    rospy.init_node('appcast_viewer', anonymous=True)
    rospy.Subscriber('/zmq/appcast',String, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()
    