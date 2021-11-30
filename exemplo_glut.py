# -*- coding: latin1 -*-
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from past.builtins import xrange

# Ângulo de rotação do objeto
ar = 0.
# Variação da rotação
dr = 1.

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


def draw():
    """
    Função que desenha os objetos
    """
    global ar, dr
    # Limpa a janela e o buffer de profundidade
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Limpa a matriz de visualização
    glLoadIdentity()
    # Move o objeto (translação)
    # Parâmetros: x, y e z (deslocamento)
    glTranslatef(-0.5, -0.5, -4.)
    # Rotação (em graus)
    # Parâmetros: graus, x, y e z (eixo)
    glRotatef(ar, 1.0 , 1.0, 1.0)
    # Mudança de escala
    # Parâmetros: x, y e z (tamanho)
    glScalef(ar / 1000, ar / 1000, ar / 1000)
    for i in xrange(0, 360, 10):
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

    # Inverte a variação
    if ar > 1000: dr = -1
    if ar < 1: dr = 1
    ar = ar + dr
    # Troca o buffer, exibindo o que acabou de ser usado
    glutSwapBuffers()

def keyboard(*args):
    """
    Função callback para tratar eventos de teclado
    """
    # Testa se a tecla ESC foi apertada
    if args[0] == '\33':
        raise SystemExit



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
    gluPerspective(45., 640. / 480., .1, 100.)
    # Seleciona a matriz de visualização
    glMatrixMode(GL_MODELVIEW)
    # Inicia o laço de eventos da GLUT
    glutMainLoop()