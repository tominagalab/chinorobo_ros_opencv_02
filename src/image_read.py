#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# IMG_PATH = '/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_02/resource/Pepper.jpg'
IMG_PATH = '/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_02/resource/Mandrill.jpg'
bgr = cv2.imread(IMG_PATH)
pub = rospy.Publisher('raw_image', Image, queue_size=10)

bridge = CvBridge()

rospy.init_node('image_read_node')
rate = rospy.Rate(1)

while not rospy.is_shutdown():
  bgr_img_msg = bridge.cv2_to_imgmsg(bgr, 'bgr8')
  pub.publish(bgr_img_msg)
  rate.sleep()
