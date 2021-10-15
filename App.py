import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *





class App:
    def __init__(self):
        self.display = (800, 600)
        self.perspective = (45, 0.1, 50.0)
        self.translate = (0, 0, -20)
        self.is_rotate = False
        self.rotate = (0, 0, 0, 0)
        self.objects_renderes = []

       

    def run(self):
        pygame.init()
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)

        gluPerspective(self.perspective[0], (self.display[0]/self.display[1]),self.perspective[1], self.perspective[2])
        glTranslatef(self.translate[0], self.translate[1], self.translate[2])
        glRotatef(self.rotate[0], self.rotate[1], self.rotate[2], self.rotate[3])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            if self.is_rotate:
                glRotatef(self.rotate[0], self.rotate[1], self.rotate[2], self.rotate[3])

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            for obj_render in self.objects_renderes:
                obj_render.show()
            pygame.display.flip()
            pygame.time.wait(10)

