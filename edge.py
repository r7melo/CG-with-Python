from pygame.constants import K_DELETE, K_END, K_HOME, K_KP_ENTER, K_PAGEDOWN, K_o
from app import App

from OpenGL.GL import *

from vector import Vector3d

import pygame



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
            vector.rotate(self.angle)
            new_verticies.append(vector.get())
            
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
            self.angle.y += 10
        if pressed[K_END]:
            self.angle.y -= 10

        # Move Right and Left X 
        if pressed[K_DELETE]:
            self.angle.x += 10
        if pressed[K_PAGEDOWN]:
            self.angle.x -= 10


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
        

edgeVerticies = (
    (0,0,0),
    (1,1,0)
)

edgeColor = (0.5,0.5,0.5)


if __name__=="__main__":
        app = App()
        app.speed = 1
        edge = Edge(edgeVerticies)
        edge.color = edgeColor
        app.render.append(edge)
        app.run()