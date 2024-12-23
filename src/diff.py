#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

pub = rospy.Publisher('output_image', Image, queue_size=10)
bridge = CvBridge()

def callback(msg):
  raw = bridge.imgmsg_to_cv2(msg)
  
  img_msg = bridge.cv2_to_imgmsg(mask, 'mono8')
  pub.publish(img_msg)

sub = rospy.Subscriber('raw_image', Image, callback)
rospy.init_node('diff_node')

rospy.spin()
