from OpenGL.GL import *

from vector import Vector3d

class Cube:
    def __init__(self):
        self.verticies = None
        self.faces = None
        self.angle = Vector3d(0,0,0)
        self.rotation = Vector3d(0,0,0)

    def rotate(self, x, y, z):
        self.angle.sum(Vector3d(x,y,z))

        if abs(self.angle.x) >= 360:
            self.angle.x = 0
        if abs(self.angle.y) >= 360:
            self.angle.y = 0
        if abs(self.angle.z) >= 360:
            self.angle.z = 0

        print(self.angle.get())

    def show(self):
        if 90 <= self.angle.x < 270:
            for face in self.faces[::-1]:
                glBegin(GL_QUADS)
                for parameter in face:
                    if type(parameter) is tuple:
                        glColor3fv(parameter)
                    elif type(parameter) is int:
                        glVertex3fv(self.verticies[parameter])
                glEnd()
        
        else:
            for face in self.faces:
                glBegin(GL_QUADS)
                for parameter in face:
                    if type(parameter) is tuple:
                        glColor3fv(parameter)
                    elif type(parameter) is int:
                        glVertex3fv(self.verticies[parameter])
                glEnd()


    def update(self):
        self.show()
        
