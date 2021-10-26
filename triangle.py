from app import App

from OpenGL.GL import *

from vector import Vector3d

import math

class Triangle:
    def __init__(self, verticies):
        self.__verticies__ = verticies
        self.verticies = verticies
        self.color = (1,1,1)
        self.angle = Vector3d(0,0,0)

    def rotate(self):
        new_verticies = []

        for vertex in self.__verticies__:
            vector = Vector3d(vertex[0], vertex[1], vertex[2])
            vector.rotate(self.angle, Vector3d())
            new_verticies.append(vector.get())
            print(new_verticies)
            
        self.verticies = tuple(new_verticies)






    def show(self):
        glBegin(GL_TRIANGLES)
        for vertex in self.verticies:
            glColor3fv(self.color)
            glVertex3fv(vertex)
        glEnd()
        


    def update(self):
        self.show()
        self.rotate()

        if abs(self.angle.x) >= 360:
            self.angle.x = 0
        if abs(self.angle.y) >= 360:
            self.angle.y = 0
        if abs(self.angle.z) >= 360:
            self.angle.z = 0

        print(self.verticies)
        
        


triangleVerticies = (
    (0,0,0),
    (1,0,0),
    (0,1,0),
)

triangle2Verticies = (
    (1,1,1),
    (2,1,1),
    (1,2,1),
)

triangleColor = (0.7,0.1,1)


if __name__=="__main__":
        from cartesian_plane import CartesianPlane
        app = App()
        app.speed = 1
        triangle = Triangle(triangleVerticies)
        triangle.color = triangleColor
        app.render.append(CartesianPlane())
        app.render.append(triangle)
        app.run()