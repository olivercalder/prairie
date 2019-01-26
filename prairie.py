#   File: prairie.py
#   Created by: Oliver Calder and Simon Parker
#   Revised 29 October 2018

from graphics import *
from random import *
from cloud import *
from mountain import *
from bison import *
import operator

class Prairie:
    def __init__(self, window, height):
        self.window=window
        self.height=height
        self.color=color_rgb(100,200,100)
        self.topL=Point(0, self.window.getHeight()-self.height)
        self.bottomR=Point(self.window.getWidth(), self.window.getHeight())
        self.rectangle=Rectangle(self.topL,self.bottomR)
        self.rectangle.setOutline(self.color)
        self.rectangle.setFill(self.color)

    def draw_prairie(self):
        self.rectangle.draw(self.window)


def main():
    window = GraphWin('Prairie', 1280, 720, autoflush=False)
    window.setBackground(color_rgb(155,200,250))
    mountains = []
    for i in range(40):
        mountain = get_rand_mnt(window)
        mountain.draw_mountain()
        mountains.append(mountain)

    clouds = []
    if randint(0,1) == 0:
        direction = 'right'
    else:
        direction = 'left'
    for n in range(2,5):
        for i in range(2**n):
            # This spawns clouds, with more clouds further away (smaller and slower), and fewer clouds closer (larger and faster)
            scale = randint(40-(n*10), 50-(n*10))/10
            cloud = get_rand_cloud(window, direction, scale)
            cloud.draw_cloud()
            clouds.append(cloud)

    prairie=Prairie(window, window.getHeight()//3)
    prairie.draw_prairie()

    bison_herds = []
    for n in range(1, 5):
        for i in range(2**n):
            # This spawns herds of bison, with more herds in the background, and fewer in the foreground
            farY = prairie.bottomR.getY() - (n * prairie.height // 4)
            nearY = prairie.bottomR.getY() - ((n-1) * prairie.height // 4)
            herd = get_bison_herd(window, prairie, farY, nearY)
            bison_herds.append(herd)
    all_bison = []
    for bison_herd in bison_herds:
        for bison in bison_herd.herd:
            all_bison.append(bison)
    bison_sorted = sorted(all_bison, key=operator.attrgetter('bottom'))
    for bison in bison_sorted:
        bison.draw_bison()

    print('Hit Crtl+C to exit ')
    while True:
        for cloud in clouds:
            cloud.step()
        for bison in bison_sorted:
            bison.step()
        update(30)

main()
