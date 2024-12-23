#!/usr/bin/env python

import rospy
import cv2

IMG_PATH = '/home/ubuntu/catkin_ws/src/chinorobo_ros_opencv_02/resource/Parrots.jpg'
bgr = cv2.imread(IMG_PATH)

hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

red = cv2.inRange(hsv, (0, 70, 0), (15, 255, 255))
blue = cv2.inRange(hsv, (90, 50, 0), (120, 255, 255))
green = cv2.inRange(hsv, (30, 80, 90), (80, 255, 255))
yellow = cv2.inRange(hsv, (20, 100, 200), (35, 255, 255))

output_red = cv2.bitwise_and(bgr, bgr, mask=red)
output_blue = cv2.bitwise_and(bgr, bgr, mask=blue)
output_green = cv2.bitwise_and(bgr, bgr, mask=green)
output_yellow = cv2.bitwise_and(bgr, bgr, mask=yellow)

cv2.imshow('bgr',bgr)
cv2.imshow('red', output_red)
cv2.imshow('blue', output_blue)
cv2.imshow('green', output_green)
cv2.imshow('yellow', output_yellow)

rospy.init_node('bgr2hsv_node')

while not rospy.is_shutdown():
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
