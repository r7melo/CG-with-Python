import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from App import App
from Cube import Cube

app = App()
app.objects_renderes.append(Cube())

app.is_rotate = True
app.rotate = (1, 3, 1, 1)
app.run()
