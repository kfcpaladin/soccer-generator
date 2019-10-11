import numpy as np
import os
import random
import cv2
from PIL import Image

save_path = 'img/'
iterations = 10000

#load images into memory
#canvas = cv2.imread("blank.bmp", cv2.IMREAD_COLOR)
#emote1 = cv2.imread("emote1.png", cv2.IMREAD_UNCHANGED)
canvas = Image.open("blank.bmp")
ball = Image.open("ball.png")

canvas.paste(ball, (random.randint(0, canvas.size[0]-ball.size[0]), random.randint(0, canvas.size[1]-ball.size[1])), ball)
canvas.show()



#for i in range(iterations):
    #rotate ball randomly.
    #place ball on to canvas
    #add distractions
    #save ball coordinates
