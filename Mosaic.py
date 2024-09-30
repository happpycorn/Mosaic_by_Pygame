import cv2
from cv2 import flip
from cv2 import resize
from cv2 import imshow
import sys
import pygame as py

py.init()

cap = cv2.VideoCapture(0)

mirro_screen = py.display.set_mode((1000,750))
screen_rect = mirro_screen.get_rect()

py.display.set_caption("mirro")

mirro_rect = py.Rect(0,0,50,50)

ltop = (30,0)
rtbm = (226, 196)

while True:

    ret,frame = cap.read()
    frame = resize(frame, (256,192))
    frame = flip(frame,1)
    img_cap = frame[ltop[1]:rtbm[1], ltop[0]: rtbm[0]]
    imshow('mirro',frame)
    img_cap = resize(frame, (20,15))
    mirro_screen.fill((255,255,255))

    for x in range(0,20):
        for y in range(0,15):
            r = img_cap[y][x][0]
            g = img_cap[y][x][1]
            b = img_cap[y][x][2]
            mirro_rect.x = x*50
            mirro_rect.y = y*50
            py.draw.rect(mirro_screen,(b,g,r),mirro_rect)


    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
    
    py.display.flip()