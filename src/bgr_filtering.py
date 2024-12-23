#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

pub = rospy.Publisher('bgr_fil_image', Image, queue_size=10)
bridge = CvBridge()

def callback(msg):
  raw = bridge.imgmsg_to_cv2(msg)
  mask = cv2.inRange(raw, (0, 128, 0), (255, 255, 255))
  output = cv2.bitwise_and(raw, raw, mask=mask)
  img_msg = bridge.cv2_to_imgmsg(output, 'bgr8')
  pub.publish(img_msg)

sub = rospy.Subscriber('raw_image', Image, callback)
rospy.init_node('bgr_filtering_node')

rospy.spin()
