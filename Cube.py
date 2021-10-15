from OpenGL.GL import *
from OpenGL.GLU import *


class Cube:
    def __init__(self):
        self.verticies = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1),
        )
        self.edges = (
            (0, 1), 
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
        )

    def show(self):
        glBegin(GL_QUADS)
        for edge in self.edges:
            glVertex2f(edge[0], edge[1])
        glEnd()
