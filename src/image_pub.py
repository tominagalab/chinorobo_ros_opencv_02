#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

IMG_PATH = '/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_02/resource/Pepper.jpg'
bgr = cv2.imread(IMG_PATH)

hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (20, 0, 0), (80, 255, 255))
output = cv2.bitwise_and(bgr, bgr, mask=mask)

rospy.init_node('image_pub_node')
rate = rospy.Rate(1)

pub_bgr = rospy.Publisher('bgr_image', Image, queue_size=10)
pub_output = rospy.Publisher('output_image', Image, queue_size=10)

bridge = CvBridge()

while not rospy.is_shutdown():
  bgr_img_msg = bridge.cv2_to_imgmsg(bgr, 'bgr8')
  output_img_msg = bridge.cv2_to_imgmsg(output, 'bgr8')
  pub_bgr.publish(bgr_img_msg)
  pub_output.publish(output_img_msg)
  rate.sleep()
