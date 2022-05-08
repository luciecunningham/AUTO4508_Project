#!/usr/bin/env/python
import rospy

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


from std_msgs.msg import String

#Waypoint Callback
def wp_cb(data):
    msg  = "caller_id: {0}\tdata: {1}".format(rospy.get_caller_id(), data.data)
    rospy.loginfo(String(msg))

#Position Callback
def vel_cb(data):
    msg  = "caller_id: {0}\tdata: {1}".format(rospy.get_caller_id(), data.data)
    rospy.loginfo(String(msg))

 

def main():
    
    #create node called waypoints
    rospy.init_node('drive')

    #Get waypoints to navigate to
    rospy.Subscriber('waypoints_comm', String, wp_cb)

    #get instantaneous velocity in x, y, z axes
    rospy.Subscriber('/RosAria/cmd_vel', Twist, vel_cb)

    #sleep until shutdown
    rospy.spin()

if __name__ == "__main__":
    main()