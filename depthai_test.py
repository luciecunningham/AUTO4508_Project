#!/usr/bin/env/python

#import depthai as dai
import rospy
from sensor_msgs.msg import Image


def image_cb(data):
    print(data.data)

def main():
    rospy.init_node('camera')

    rospy.Subscriber('/stereo_publisher/right/image', Image, image_cb)

    rospy.spin()



if __name__ == "__main__":
    main()