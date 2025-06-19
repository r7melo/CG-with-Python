from pygame.constants import K_DELETE, K_END, K_HOME, K_PAGEDOWN
from app import App

from OpenGL.GL import *
from cartesian_plane import CartesianPlane

from vector import Vector3d

from math import *


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
        

        

    def update(self):
        # self.circle(angle_y=self.rotation_y, angle_x=self.rotation_x, rain=5)
        # self.rotation_y += 1

        ambiente = [1.0, 1.0, 1.0, 1.0]
        glShadeModel(GL_FLAT)
        glEnable(GL_COLOR_MATERIAL)
        glLightfv (GL_LIGHT0, GL_AMBIENT, ambiente)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)

        especular = [1.0, 1.0, 1.0, 1.0]
        position = [0.0, 3.0, 1.0, 0.0 ]
        glShadeModel(GL_FLAT)
        glEnable(GL_COLOR_MATERIAL)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, especular)
        glMaterialf (GL_FRONT_AND_BACK, GL_SHININESS, 20.0)
        glLightfv (GL_LIGHT0, GL_SPECULAR, especular)
        glLightfv (GL_LIGHT0, GL_POSITION, position)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)


if __name__=="__main__":
        from cartesian_plane import CartesianPlane
        app = App()
        app.screenSize = (900, 900)
        app.render.append(CartesianPlane())
        app.render.append(Circle())
        app.run()