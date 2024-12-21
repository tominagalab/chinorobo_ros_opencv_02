#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


IMG_PATH = "/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_02/resource/Mandrill.jpg"

rospy.init_node("chinorobo_opencv")
rate = rospy.Rate(0.5)

pub = rospy.Publisher('/raw_image', Image, queue_size=5)

src = cv2.imread(IMG_PATH)
bridge = CvBridge()
src_msg = bridge.cv2_to_imgmsg(src, 'bgr8')

while not rospy.is_shutdown():
  pub.publish(src_msg)
  rate.sleep() 
  

cv2.destroyAllWindows()