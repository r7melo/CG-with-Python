from pygame.constants import K_DELETE, K_END, K_HOME, K_PAGEDOWN
from app import App

from OpenGL.GL import *
from cartesian_plane import CartesianPlane

from vector import Vector3d

import pygame
import math


class Edge:
    def __init__(self, verticies):
        self.__verticies__ = verticies
        self.verticies = verticies
        self.color = (1,1,1)
        self.angle = Vector3d(0,0,0)

    def rotate(self):
        new_verticies = []

        

        for vertex in self.__verticies__:
            vector = Vector3d(vertex[0], vertex[1], vertex[2])
            vector.rotate(self.angle, Vector3d(0.5,0.5,0.5))
            new_verticies.append(vector.get())

        self.angle.z += 1
    
        print(new_verticies)
        
        self.verticies = tuple(new_verticies)
            



    def show(self):
        glBegin(GL_LINES)
        for vertex in self.verticies:
            glColor3fv(self.color)
            glVertex3fv(vertex)
        glEnd()
        
    def keyboard(self):
        pressed = pygame.key.get_pressed()
        
        # Move Up and Down Y
        if pressed[K_HOME]:
            self.angle.y += 0.1
        if pressed[K_END]:
            self.angle.y -= 0.1

        # Move Right and Left X 
        if pressed[K_DELETE]:
            self.angle.x -= 0.1
        if pressed[K_PAGEDOWN]:
            self.angle.x += 0.1


    def update(self):
        self.show()
        self.rotate()
        self.keyboard()

        if abs(self.angle.x) >= 360:
            self.angle.x = 0
        if abs(self.angle.y) >= 360:
            self.angle.y = 0
        if abs(self.angle.z) >= 360:
            self.angle.z = 0
        

edgeVerticies1 = (
    (0,0,0),
    (1,0,0)
)

edgeVerticies2 = (
    (0,0,0),
    (0,1,0)
)

edgeVerticies3 = (
    (0,0,0),
    (0,0,1)
)

edgeColor = (0.5,0.5,0.5)


if __name__=="__main__":
        from cartesian_plane import CartesianPlane
        app = App()

        edge1 = Edge(edgeVerticies1)
        edge2 = Edge(edgeVerticies2)
        edge3 = Edge(edgeVerticies3)

        app.render.append(CartesianPlane())
        app.render.append(edge1)
        app.render.append(edge2)
        app.render.append(edge3)

        app.run()