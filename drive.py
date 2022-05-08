#!/usr/bin/env/python
import rospy


from std_msgs.msg import String

#Waypoint Callback
def wp_cb(data):
    msg  = "caller_id: {0}\tdata: {1}".format(rospy.get_caller_id(), data.data)
    rospy.loginfo(String(msg))

def pos_cb(data):
    msg  = "caller_id: {0}\tdata: {1}".format(rospy.get_caller_id(), data.data)
    rospy.loginfo(String(msg))

    

def main():
    
    #create node called waypoints
    rospy.init_node('drive')

    rospy.Subscriber('waypoints_comm', String, wp_cb)
    rospy.Subscriber('positions_comm', String, pos_cb)

    #sleep until shutdown
    rospy.spin()

if __name__ -- "__main__":
    main()