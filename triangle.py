from OpenGL.GL import *

from vector import Vector3d

import math

class Triangle:
    def __init__(self):
        self.verticies = None
        self.color = (1,1,1)
        self.angle = Vector3d(0,0,0)
        self.rotation = Vector3d(0,0,0)

    def rotate(self, x, y, z):
        new_verticies = []
        if z > 0:
            for vertex in self.verticies:
                pass



    def show(self):
        glBegin(GL_TRIANGLES)
        for vertex in self.verticies:
            glColor3fv(self.color)
            glVertex3fv(vertex)
        glEnd()
        


    def update(self):
        self.show()
        
