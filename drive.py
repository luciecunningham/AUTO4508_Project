#!/usr/bin/env/python

import rospy

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import NavSatFix

from std_msgs.msg import String

import numpy as np


WAYPOINTS = [[0,0], [1,1]]

"""
#Waypoint Callback
def wp_cb(data):
    global wp_x
    global wp_y
    msg  = "caller_id: {0}\tdata: {1}".format(rospy.get_caller_id(), data.data)
    rospy.loginfo(String(msg))
    wp_x = data
"""


def coords_cb(data):
    global cur_lat
    global cur_lon
    msg  = "caller_id: {0}\tdata: {1}".format(rospy.get_caller_id(), data.data)
    rospy.loginfo(String(msg))
    cur_lat = data.latitude
    cur_lon = data.longitude



def get_cartesian(lat,lon):

    rlat = np.deg2rad(lat)
    rlon = np.deg2rad(lon)
    RADIUS = 6378000
    x = RADIUS * np.cos(rlat) * np.cos(rlon)
    y = RADIUS * np.cos(rlat) * np.sin(rlon)
    return x,y

def get_vector(x1,y1,x2,y2):
    dist_x = x2 - x1
    dist_y = y2 - y1
    dist = np.sqrt(dist_x * dist_x + dist_y * dist_y)

    angle = np.rad2deg(np.atan2(dist_x, dist_y))

    return dist, angle

def create_twist(dist,angle):
    twist_msg = Twist()

    twist_msg.linear.x = dist
    twist_msg.linear.y = 0
    twist_msg.linear.z = 0

    twist_msg.angular.x = 0
    twist_msg.angular.y = 0
    twist_msg.angular.z = angle

    return twist_msg

def waypoint_drive():
    #send instantaneous velocity in x, y, z axes
    vel_pub = rospy.Publisher('/RosAria/cmd_vel', Twist)

    accuracy = 10
    
    while not((cur_lat <= wp_lat + accuracy and cur_lat >= wp_lat - accuracy) and (cur_lon <= wp_lon + accuracy and cur_lon >= wp_lon - accuracy)):
        dist, angle = get_vector(get_cartesian(cur_lat, cur_lon), get_cartesian(wp_lat, wp_lon))
        twist_msg = create_twist(dist,angle)
        vel_pub.publish(twist_msg)
        rospy.Subscriber('/fix', NavSatFix, coords_cb)
        #Check for bucket



def main():
    global wp_lat
    global wp_lon
    global cur_lat
    global cur_lon

    #create node called waypoints
    rospy.init_node('drive')

    rospy.Subscriber('/fix', NavSatFix, coords_cb)

    #Go to each waypoint
    for waypoint in WAYPOINTS:
        wp_lat = waypoint[0]
        wp_lon = waypoint[1]
        waypoint_drive()

        #Take picture here

    #return to start
    wp_lat = WAYPOINTS[0][0]
    wp_lon = WAYPOINTS[0][1]
    waypoint_drive()


    #sleep until shutdown
    rospy.spin()

if __name__ == "__main__":
    main()