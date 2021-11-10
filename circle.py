from pygame.constants import K_DELETE, K_END, K_HOME, K_PAGEDOWN
from app import App

from OpenGL.GL import *
from cartesian_plane import CartesianPlane

from vector import Vector3d

import pygame
from math import *

from cube import Cube

class Circle:
    def __init__(self):
        self.rotation_x = 0
        self.rotation_y = 0

    def spin(self, x,y, angle):
        return ((y * cos((angle/180)*pi)) - (x * sin((angle/180)*pi)), (y * sin((angle/180)*pi)) + (x * cos((angle/180)*pi)))



    def circle(self, x=0, y=0, z=0, rain=0, angle_x=0, angle_y=0):
        glColor3f(0,1,0.7)

        spiny = (0,0)
        if angle_y > 0:
            spiny = self.spin(0,rain,angle_y)

        spinx = (0,0)
        if angle_x > 0:
            spinx = self.spin(0,rain,angle_x)

        
        Cube(spiny[0] ,spiny[1], spinx[0])
        

        

    def update(self):
        self.circle(angle_y=self.rotation_y, angle_x=self.rotation_x, rain=5)
        self.rotation_y += 1


if __name__=="__main__":
        from cartesian_plane import CartesianPlane
        app = App()
        app.screenSize = (900, 900)
        app.render.append(CartesianPlane())
        app.render.append(Circle())
        app.run()