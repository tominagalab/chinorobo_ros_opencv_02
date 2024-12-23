#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

pub = rospy.Publisher('nose_and_cheek_image', Image, queue_size=10)
bridge = CvBridge()

def callback(msg):
  raw = bridge.imgmsg_to_cv2(msg)
  hsv = cv2.cvtColor(raw, cv2.COLOR_BGR2HSV)

  mask1 = cv2.inRange(hsv, (0, 100, 0), (10, 255, 255))
  mask2 = cv2.inRange(hsv, (150, 50, 0), (180, 255, 255))
  nose_mask = cv2.bitwise_or(mask1, mask2)
  
  cheek_mask = cv2.inRange(hsv, (98, 30, 170), (120, 255, 255))

  mask = cv2.bitwise_or(nose_mask, cheek_mask)
  output = cv2.bitwise_and(raw, raw, mask=mask)
  
  img_msg = bridge.cv2_to_imgmsg(output, 'bgr8')
  pub.publish(img_msg)

sub = rospy.Subscriber('raw_image', Image, callback)
rospy.init_node('nose_and_cheek_node')

rospy.spin()
