# -*- coding: utf-8 -*-
# @Time    : 21-07-2020 12:04 AM
# @Author  : Mohammad Akram
# @Email   : akramtoday@gmail.com

# Provide an image to know RGB values for any number of points
# press ESC to exit

import cv2

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONUP:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue)+", "+str(green)+","+str(red)
        cv2.putText(img, strBGR, (x,y), font, 0.5, (0,255,255), 2)


img_path = input("Enter the Image Path: ")
# img_path = r'.\peppers.png'
img = cv2.imread(img_path)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
cv2.imshow('image', img)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
