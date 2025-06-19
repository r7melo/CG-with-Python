from app import App

from OpenGL.GL import *
from OpenGL.GLU import *


vertices = (
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1)
)

edges = (
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

class Cube:
	def __init__(self, tX, tY, tZ):
		glBegin(GL_LINES)
		for edge in edges:
			for vertex in edge:
				glVertex3f(vertices[vertex][0] + tX, vertices[vertex][1] + tY, vertices[vertex][2] + tZ)
		glEnd()



class CubesOnSpace:
	def update(self):
		for i in range(8):
			for j in range(8):
				Cube(-i , -4, -j )

if __name__=="__main__":
	app = App()
	cubes_on_space = CubesOnSpace()
	app.render.append(cubes_on_space) 
	app.run()