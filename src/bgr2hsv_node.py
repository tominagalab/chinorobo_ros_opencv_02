#!/usr/bin/env python

import rospy
import cv2

IMG_PATH = '/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_02/resource/Parrots.jpg'
bgr = cv2.imread(IMG_PATH)

hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

green = cv2.inRange(hsv, (20, 0, 0), (80, 255, 255))

output = cv2.bitwise_and(bgr, bgr, mask=green)

cv2.imshow('bgr',bgr)
cv2.imshow('output', output)

rospy.init_node('bgr2hsv_node')

while not rospy.is_shutdown():
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
