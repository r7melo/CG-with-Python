import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from cube import Cube
from triangle import Triangle
from constants import *
from vector import Vector3d

class App:
    def __init__(self):
        self.keyboard = None
        self.display = (0, 0)
        self.fovy = 0
        self.aspect = 0
        self.z_near = 0
        self.z_far = 0
        self.angle = 0
        self.translation = Vector3d()
        self.rotation = Vector3d()



    def run(self):
        pygame.init()
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        gluPerspective(self.fovy, (self.display[0]/self.display[1]), self.z_near, self.z_far)
        glTranslatef(self.translation.x, self.translation.y, self.translation.z)

        #============================================================================
        triangle = Triangle()
        triangle.color = triangleColor
        triangle.verticies = triangleVerticies
        #============================================================================
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            
            #============================================================================
            
            triangle.show()
            

            #============================================================================

            keys = pygame.key.get_pressed()
        
            if keys[K_UP]:
                glRotatef(1,1,0,0)
                triangle.rotate(1,0,0)
            elif keys[K_DOWN]:
                glRotatef(1,-1,0,0)
                triangle.rotate(-1,0,0)
            if keys[K_RIGHT]:
                glRotatef(1,0,1,0)
                triangle.rotate(0,1,0)
            elif keys[K_LEFT]:
                glRotatef(1,0,-1,0)
                triangle.rotate(1,-1,0)

            if keys[K_q]:
                glTranslatef(0,0,-0.1)
            elif keys[K_e]:
                glTranslatef(0,0,0.1)
            
            if keys[K_w]:
                glTranslatef(0,-0.1,0)
            elif keys[K_s]:
                glTranslatef(0,0.1,0)

            if keys[K_a]:
                glTranslatef(-0.1,0,0)
            elif keys[K_d]:
                glTranslatef(0.1,0,0)

            print
                

            pygame.display.flip()
            pygame.time.wait(10)
