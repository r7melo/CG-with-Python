# -*- coding: latin1 -*-
import math
import pygame
from pygame.locals import *
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from past.builtins import xrange

from cartesian_plane import CartesianPlane

# Ângulo de rotação do objeto
angle = 0.
# Variação da rotação
speed_angle = 1.
# Valores cartesianos de rotacao
angle_x = 0
angle_y = 0
angle_z = 0

def resize(x, y):
    """
    Função callback que é evocada quando
    a janela muda de tamanho
    """

    # Limpa a vista
    glViewport(0, 0, x, y)
    # Seleciona a matriz de projeção
    glMatrixMode(GL_PROJECTION)
    # Limpa a matriz de projeção
    glLoadIdentity()

    # Calcula o aspecto da perspectiva
    gluPerspective(45., float(x)/float(y), 0.1, 100.0)

    # Seleciona a matriz de visualização
    glMatrixMode(GL_MODELVIEW)


# funcao de desenhar uma esfera
def esfera(rain, nStacks, nSectors):
    # geracao de pontos ==
    pontos = []

    deltaPhi = math.pi/nStacks
    deltaTheta = 2*math.pi/nSectors

    for i in xrange(nStacks):
        phi = -math.pi/2*i*deltaPhi
        temp = rain * math.cos(phi)
        y = rain * math.sin(phi)
        
        for j in xrange(nSectors):
            theta = j*deltaTheta
            x =  temp*math.sin(theta)
            z =  temp*math.cos(theta)

            if z > 0: pontos.append((x,y,z))
    
    # geracao de pontos
    glColor3f(1,0,0)
    glPointSize(2.5)
    glBegin(GL_POINTS)
    for ponto in pontos:
        glVertex3fv(ponto)
    glEnd()


def draw():
    """
    Função que desenha os objetos
    """
    global angle, angle_y, angle_x, angle_z
    # Limpa a janela e o buffer de profundidade
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Limpa a matriz de visualização
    glLoadIdentity()
    # Move o objeto (translação)
    # Parâmetros: x, y e z (deslocamento)
    glTranslatef(-0.5, -0.5, -4.)
    # Rotação (em graus)
    # Parâmetros: graus, x, y e z (eixo)
    glRotatef(angle, angle_x , angle_y, angle_z)
    # Mudança de escala
    # Parâmetros: x, y e z (tamanho)
    glScalef(1, 1, 1)

    for i in xrange(0, 100, 10):
        # Rotação das faces do objeto
        glRotatef(10, 1.0 , 1.0, 1.0)
        # Inicia a criação de uma face retangular
        glBegin(GL_QUADS)

        # Define a cor que será usada para desenhar (R, G, B)
        glColor3f(.7, .5, .1)
        # Cria um vértice da face
        glVertex3f(0., 0., 0.)
        glColor3f(.7, .3, .1)
        glVertex3f(1., 0., 0.)
        glColor3f(.5, .1, .1)
        glVertex3f(1., 1., 0.)
        glColor3f(.7, .3, .1)
        glVertex3f(0., 1., 0.)
        # Termina a face
        glEnd()

    #================================================================================================== criacao do poligono 

    CartesianPlane().update()

    glLoadIdentity()
    glPushMatrix()
    glTranslatef(-20, 0, -50)
    glRotatef(angle, 0, 1, 0)
    esfera(10, 50, 50)
    glPopMatrix()
    angle += 1

    #================================================================================================== criacao do poligono


    # Inverte a variação
    # if ar > 1000: dr = 0.01
    # if ar < 1: dr = 1
    # ar = ar + dr

    # Troca o buffer, exibindo o que acabou de ser usado
    glutSwapBuffers()

def keyboard(*args):
    """
    Função callback para tratar eventos de teclado
    """
    # Testa se a tecla ESC foi apertada
    if args[0] == b'\x1b':
        raise SystemExit

    global angle, speed_angle, angle_x, angle_z, angle_z
    # Teclas de Rotacao do chunk
    if args[0] == b'a':
        angle += speed_angle
    if args[0] == b'd':
        angle -= speed_angle
    if args[0] == b'w':
        pass
    if args[0] == b's':
        pass
    



if __name__ == '__main__':
    # Inicializa a GLUT
    glutInit(argv)
    # Seleciona o modo de exibição
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    # Configura a resolução da janela do GLUT de 640 x 480
    glutInitWindowSize(640, 480)
    # Cria a janela do GLUT
    window = glutCreateWindow('A')
    # Configura a função callback que desenha na janela atual

    glutDisplayFunc(draw)
    # Para exibir em tela cheia
    glutFullScreen()
    # Registra a função para tratar redesenhar a janela quando
    # não há nada a fazer
    glutIdleFunc(draw)
    # Registra a função para redesenhar a janela quando
    # ela for redimensionada
    glutReshapeFunc(resize)
    # Registra a função para tratar eventos de teclado
    glutKeyboardFunc(keyboard)
    # Inicialização da janela
    # Limpa a imagem (fundo preto)
    glClearColor(0., 0., 0., 0.)
    # Limpa o buffer de profundidade
    glClearDepth(1.)

    # Configura o tipo do teste de profundidade
    glDepthFunc(GL_LESS)
    # Ativa o teste de profundidade
    glEnable(GL_DEPTH_TEST)
    # Configura o sombreamento suave
    glShadeModel(GL_SMOOTH)
    # Seleciona a matriz de projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(15., 640. / 480., .1, 100.)
    # Seleciona a matriz de visualização
    glMatrixMode(GL_MODELVIEW)
    # Inicia o laço de eventos da GLUT
    glutMainLoop()