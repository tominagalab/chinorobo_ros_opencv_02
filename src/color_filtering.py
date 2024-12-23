#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

pub = rospy.Publisher('output_image', Image, queue_size=10)
bridge = CvBridge()

def callback(msg):
  raw = bridge.imgmsg_to_cv2(msg)
  hsv = cv2.cvtColor(raw, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv, (30, 80, 90), (80, 255, 255))
  output = cv2.bitwise_and(raw, raw, mask=mask)
  img_msg = bridge.cv2_to_imgmsg(output, 'bgr8')
  pub.publish(img_msg)

sub = rospy.Subscriber('raw_image', Image, callback)
rospy.init_node('color_filtering_node')

rospy.spin()
