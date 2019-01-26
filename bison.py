#   File: bison.py
#   Created by: Oliver Calder and Simon Parker
#   Revised 29 October 2018

from graphics import *
from random import *

class Bison:

    def __init__(self, window, prairie, x, y, speed, true_size, scale, direction):
        self.window = window
        self.prairie = prairie
        self.x = x
        self.y = y
        self.center = Point(self.x, self.y)
        self.true_size = true_size
        self.scale = (self.center.getY() - prairie.topL.getY()) / prairie.height
        self.speed = speed
        self.size = self.true_size * self.scale
        self.bottom = self.center.getY()+20*self.size
        self.direction = direction
        self.red = randint(80, 160)
        self.green = self.red // 2
        self.color = color_rgb(self.red, self.green, 0)

        if direction == 'right':
            self.sign = 1
        elif direction == 'left':
            self.sign = (-1)

        self.rrLeg = Rectangle(Point(self.center.getX()-self.sign*22*self.size, self.center.getY()), Point(self.center.getX()-self.sign*18*self.size, self.center.getY()+20*self.size))
        self.rlLeg = Rectangle(Point(self.center.getX()-self.sign*16*self.size, self.center.getY()), Point(self.center.getX()-self.sign*12*self.size, self.center.getY()+18*self.size))
        self.frLeg = Rectangle(Point(self.center.getX()+self.sign*10*self.size, self.center.getY()), Point(self.center.getX()+self.sign*14*self.size, self.center.getY()+20*self.size))
        self.flLeg = Rectangle(Point(self.center.getX()+self.sign*16*self.size, self.center.getY()), Point(self.center.getX()+self.sign*20*self.size, self.center.getY()+18*self.size))
        self.torso = Oval(Point(self.center.getX()-self.sign*20*self.size, self.center.getY()-10*self.size), Point(self.center.getX()+self.sign*20*self.size, self.center.getY()+10*self.size))
        self.shoulders = Oval(Point(self.center.getX()+self.sign*6*self.size, self.center.getY()-10*self.size), Point(self.center.getX()+self.sign*22*self.size, self.center.getY()+14*self.size))
        self.tail = Line(Point(self.center.getX()-self.sign*22*self.size, self.center.getY()-2*self.size), Point(self.center.getX()-self.sign*28*self.size, self.center.getY()+8*self.size))
        self.tail.setWidth(2*self.size)
        self.hips = Oval(Point(self.center.getX()-self.sign*24*self.size, self.center.getY()-8*self.size), Point(self.center.getX()-self.sign*8*self.size, self.center.getY()+10*self.size))
        self.back = Oval(Point(self.center.getX()-self.sign*2*self.size, self.center.getY()-14*self.size), Point(self.center.getX()+self.sign*22*self.size, self.center.getY()))
        self.head = Oval(Point(self.center.getX()+self.sign*20*self.size, self.center.getY()-10*self.size), Point(self.center.getX()+self.sign*32*self.size, self.center.getY()+6*self.size))
        self.hornL = Line(Point(self.center.getX()+self.sign*28*self.size, self.center.getY()-4*self.size), Point(self.center.getX()+self.sign*26*self.size, self.center.getY()-4*self.size))
        self.hornL.setWidth(2*self.size)
        self.hornM = Line(Point(self.center.getX()+self.sign*26*self.size, self.center.getY()-4*self.size), Point(self.center.getX()+self.sign*24*self.size, self.center.getY()-6*self.size))
        self.hornM.setWidth(1.7*self.size)
        self.hornU = Line(Point(self.center.getX()+self.sign*24*self.size, self.center.getY()-6*self.size), Point(self.center.getX()+self.sign*24*self.size, self.center.getY()-8*self.size))
        self.hornU.setWidth(1.4*self.size)
        self.hornT = Line(Point(self.center.getX()+self.sign*24*self.size, self.center.getY()-8*self.size), Point(self.center.getX()+self.sign*26*self.size, self.center.getY()-10*self.size))
        self.hornT.setWidth(1*self.size)
        self.eye = Circle(Point(self.center.getX()+self.sign*28*self.size, self.center.getY()-2*self.size), 1*self.size)
        self.nose = Circle(Point(self.center.getX()+self.sign*30*self.size, self.center.getY()+2*self.size), 2*self.size)

        self.bison = [self.rrLeg, self.rlLeg, self.frLeg, self.flLeg, self.torso, self.shoulders, self.tail, self.hips, self.back, self.head, self.hornL, self.hornM, self.hornU, self.hornT, self.eye, self.nose]

    def draw_bison(self):
        for part in self.bison:
            part.setFill(self.color)
            part.setOutline(self.color)
            if part == self.hornL or part == self.hornM or part == self.hornU or part == self.hornT:
                part.setFill('white')
                part.setOutline('white')
            if part == self.nose or part == self.eye:
                part.setFill('black')
                part.setOutline('black')
            part.draw(self.window)

    def step(self):
        if self.direction == 'right':
            self.center.move(self.speed, 0)
            for part in self.bison:
                part.move(self.speed, 0)
            if self.center.getX() > self.window.getWidth() + (100 * self.scale):
                self.center.move((self.window.getWidth()+200*self.scale)*-1, 0)
                for part in self.bison:
                    part.move((self.window.getWidth()+200*self.scale)*-1, 0)
        elif self.direction == 'left':
            self.center.move(0 - self.speed, 0)
            for part in self.bison:
                part.move(0 - self.speed, 0)
            if self.center.getX() < (-100 * self.scale):
                self.center.move((self.window.getWidth()+200*self.scale), 0)
                for part in self.bison:
                    part.move((self.window.getWidth()+200*self.scale), 0)

class Bison_herd:

    def __init__(self, window, prairie, x, y, true_speed, number, direction):
        self.window = window
        self.prairie = prairie
        self.x = x
        self.y = y
        self.center = Point(self.x, self.y)
        self.true_speed = true_speed
        self.scale = (self.center.getY() - self.prairie.topL.getY()) / self.prairie.height
        self.speed = self.true_speed * self.scale
        self.number = number
        self.direction = direction
#        if direction == 'right':
#            self.velocity = self.speed
#        elif direction == 'left':
#            self.velocity = 0 - self.speed

        self.herd = []
        for i in range(self.number):
            size_index = randint(1,3)
            if size_index == 1:
                true_size = randint(10,20)/10
            else:
                true_size = 2

            bison_x = randint(self.x - int(200*self.scale), self.x + int(200*self.scale))
            bison_y = randint(self.y - int(30*self.scale), self.y + int(30*self.scale))
            bison = Bison(self.window, self.prairie, bison_x, bison_y, self.speed, true_size, self.scale, self.direction)
            self.herd.append(bison)

    def draw_herd(self):
        for bison in self.herd:
            bison.draw_bison()

    def step(self):
        if self.direction == 'right':
            self.center.move(self.speed, 0)
        elif self.direction == 'left':
            self.center.move(0 - self.speed, 0)
        for bison in self.herd:
            bison.step()

def get_bison_herd(window, prairie, farY, nearY):
    if randint(1, 2) == 1:
        direction = 'right'
    else:
        direction = 'left'
    x = randint(0, window.getWidth())
    y = randint(farY, nearY)
    number = randint(5, 20)
    true_speed = randint(10, 30)/10
    herd = Bison_herd(window, prairie, x, y, true_speed, number, direction)
    return herd
