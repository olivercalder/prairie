#   File: cloud.py
#   Created by: Oliver Calder and Simon Parker
#   Revised 29 October 2018

from graphics import *
from random import *
import time


class Cloud:
    def __init__(self, window, true_radius, x, y, scale, true_speed, direction):
        self.window = window
        self.true_radius = true_radius
        self.x = x
        self.y = y
        self.scale = scale
        self.true_speed = true_speed
        self.direction = direction
        self.color = color_rgb(240,240,240)

        self.radius = self.true_radius * self.scale
        self.poof_radius = self.radius // 2
        self.speed = self.true_speed * self.scale

        self.topLX = self.x-(self.radius//randint(2,4))
        self.topLY = self.y-(self.radius//randint(1,4))
        self.topL = Circle(Point(self.topLX, self.topLY), self.poof_radius)

        self.topRX = self.x-(self.radius//randint(2,4))
        self.topRY = self.y-(self.radius//randint(1,4))
        self.topR = Circle(Point(self.topRX, self.topRY), self.poof_radius)

        self.leftX = self.x-(int(self.radius/(randint(10,17)/10)))
        self.leftY = self.y-(self.radius//randint(1,4))
        self.left = Circle(Point(self.leftX, self.leftY), self.poof_radius)

        self.middleX = self.x
        self.middleY = self.y-(self.radius//randint(1,4))
        self.middle = Circle(Point(self.middleX, self.middleY), self.poof_radius)

        self.rightX = self.x+(int(self.radius/(randint(10,17)/10)))
        self.rightY = self.y-(self.radius//randint(1,4))
        self.right = Circle(Point(self.rightX, self.rightY), self.poof_radius)

        self.cloud = [self.topL, self.topR, self.left, self.middle, self.right]

    def draw_cloud(self):
        for part in self.cloud:
            part.setOutline(self.color)
            part.setFill(self.color)
            part.draw(self.window)

    def step(self):
        speed = self.speed
        if self.direction == 'right':
            back_speed = (-1 * self.window.getWidth()) - (self.radius * 3)
        elif self.direction == 'left':
            back_speed = self.window.getWidth() + (self.radius * 3)
        for part in self.cloud:
            if self.direction == 'right':
                if part.getCenter().getX() <= self.window.getWidth() + (part.radius * 2):
                    part.move(speed,0)
                else:
                    part.move(back_speed,0)
            elif self.direction == 'left':
                if part.getCenter().getX() >= -1 * (part.radius * 2):
                    part.move(speed,0)
                else:
                    part.move(back_speed,0)




def get_rand_cloud(window, direction, scale):
    true_speed = randint(10, 20)/40
    if direction == 'left':
        true_speed = true_speed * -1
    true_radius = randint(window.getHeight()//45, window.getHeight()//12)
    x = randint(0, window.getWidth())
    y = randint(window.getHeight()//16, int(window.getHeight()/2))
    cloud = Cloud(window,true_radius,x,y,scale,true_speed,direction)
    return cloud
