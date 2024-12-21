#!/usr/bin/env python

import rospy
import cv2

IMG_PATH = "/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_02/resource/Mandrill.jpg"

rospy.init_node("bgr_to_hsv")
rate = rospy.Rate(1)

src = cv2.imread(IMG_PATH)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

while not rospy.is_shutdown():
  
  cv2.imshow('src', src)
  cv2.imshow('hsv', hsv)
  
  if cv2.waitKey(1) == 27:
    break
  
cv2.destroyAllWindows()