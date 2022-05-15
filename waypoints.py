#!/usr/bin/env/python
import rospy

from sensor_msgs.msg import NavSatFix


def get_waypoints():
    x,y = 0,0
    return (x,y)

def publish_waypoints(pub, waypoint):
    """
    args:   publisher == node publisher
            waypoint == list of a coord, waypoint[0] is x and waypoint[1] is y
    """
    waypoint_str = String("waypoint: x:{0}, y:{1}".format(waypoint[0], waypoint[1]))
    rospy.loginfo(waypoint_str)
    pub.publish(waypoint_str)
    
    

def main():
    
    pub = rospy.Publisher('waypoints_comm', NavSatFix, queue_size=10)

    #create node called waypoints
    rospy.init_node('waypoint')

    #loop every 1/10 seconds
    rate = rospy.Rate(10)


    while not rospy.is_shutdown():
        #callbacks here
        curr_waypoint = get_waypoints()
        publish_waypoints(pub, curr_waypoint)

        rate.sleep()
        #sleep until shutdown
        



if __name__ == "__main__":
    main()