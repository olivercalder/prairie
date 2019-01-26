#   File: mountain.py
#   Created by: Oliver Calder and Simon Parker
#   Revised 29 October 2018

from graphics import *
from random import *

class Mountain:
    def __init__(self, window, height, width, position,color):
        self.height = height
        self.width = width
        self.position = position
        self.window = window
        self.color = color
        self.peak = Point(self.position, self.window.getHeight()-self.height)
        self.left = Point(self.position-(int(self.width*(randint(25,100)/100))), int(self.window.getHeight()/1.5))
        self.right = Point(self.position+(int(self.width*(randint(25,100)/100))), int(self.window.getHeight()/1.5))
        self.triangle = Polygon(self.peak,self.left,self.right)
        self.triangle.setFill(self.color)
        self.triangle.setOutline(self.color)

    def draw_mountain(self):
        self.triangle.draw(self.window)


def get_rand_color_mnt():
    red = randint(165, 215)
    grn = randint(165, 215)
    blu = randint(185, 235)
    return color_rgb(red, grn, blu)

def get_rand_mnt(window):
    height = randint(int(window.getHeight()/1.9), int(window.getHeight()*(6/7)))
    width = randint(height//3, int(height*2))
    position = randint(-1*width, window.getWidth()+(width))
    color = get_rand_color_mnt()
    mountain = Mountain(window,height,width,position,color)
    return mountain
