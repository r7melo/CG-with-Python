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
        cube = Cube()
        cube.verticies = cuboVerticies
        cube.faces = cuboFaces

        triangle = Triangle(triangleVerticies)
        triangle.color = triangleColor

        triangle2 = Triangle(triangle2Verticies)
        triangle2.color = (0.1,1,0)
        #============================================================================
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            #glRotatef(1, 1,1,0)

            glBegin(GL_LINES)
            glColor3fv((0,0,0.1))
            glVertex3fv((0,0,-10))
            glVertex3fv((0,0,10))
            
            glColor3fv((0,0.1,0))
            glVertex3fv((0,-10,0))
            glVertex3fv((0,10,0))

            glColor3fv((0.1,0,0))
            glVertex3fv((-10,0,0))
            glVertex3fv((10,0,0))
            glEnd()
            
            
            #============================================================================
            
            #cube.show()
            triangle.update()
            triangle2.update()


            print(triangle.angle.get(), triangle.verticies)
            

            #============================================================================

            keys = pygame.key.get_pressed()
        
            if keys[K_w]:
                triangle.angle.x += 10
                triangle2.angle.x += 10
            elif keys[K_s]:
                triangle.angle.x -= 10
                triangle2.angle.x -= 10
            if keys[K_d]:
                triangle.angle.y += 10
                triangle2.angle.y += 10
            elif keys[K_a]:
                triangle.angle.y -= 10
                triangle2.angle.y -= 10
            if keys[K_q]:
                triangle.angle.z += 10
                triangle2.angle.z += 10
            elif keys[K_e]:
                triangle.angle.z -= 10
                triangle2.angle.z -= 10


            if keys[K_PAGEUP]:
                pass
            elif keys[K_PAGEDOWN]:
                pass
                

            pygame.display.flip()
            pygame.time.wait(100)
