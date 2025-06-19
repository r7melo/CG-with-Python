# -*- coding: latin1 -*-
from sys import argv
from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    """
    Função callback que desenha na janela
    """

    # glClear limpa a janela com valores pré-determinados
    # GL_COLOR_BUFFER_BIT define que o buffer aceita escrita de cores
    # GL_DEPTH_BUFFER_BIT define que o buffer de profundidade será usado
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rgba = [.8, .6, .4, .9]
    # glMaterial especifica os parâmetros do material que serão
    # usados no modelo de iluminação da cena (no formato RGBA)
    # GL_FRONT define que a face afetada pela função é a frontal
    # GL_AMBIENT especifica que o parâmetro é a reflexão de ambiente
    glMaterialfv(GL_FRONT, GL_AMBIENT, rgba)
    # GL_DIFFUSE especifica que o parâmetro é a reflexão difusa do material
    glMaterialfv(GL_FRONT, GL_DIFFUSE, rgba)
    # GL_SPECULAR especifica que o parâmetro é a reflexão especular
    glMaterialfv(GL_FRONT, GL_SPECULAR, rgba)
    # GL_EMISSION especifica que o parâmetro é a emissão do material
    # glMaterialfv(GL_FRONT, GL_EMISSION, rgba)
    # GL_SHININESS especifica o expoente usado pela reflexão especular
    glMaterialfv(GL_FRONT, GL_SHININESS, 120)
    # Desenha uma esfera sólida, com raio 0.5 e 128 divisões
    # na horizontal e na vertical
    glutSolidSphere(0.5, 128, 128)
    # Força a execução dos comandos da OpenGL
    glFlush()


# Inicializa a biblioteca GLUT
glutInit(argv)
# glutInitDisplayMode configura o modo de exibição
# GLUT_SINGLE define o buffer como simples
# (também pode ser duplo, com GLUT_DOUBLE)
# GLUT_RGB seleciona o modo RGB
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
# Cria a janela principal
glutCreateWindow('Esfera')
# Configura a função callback que desenha na janela atual
glutDisplayFunc(display)
# Limpa a janela com a cor especificada
glClearColor(.25, .15, .1, 1.)
# Muda a matriz corrente para GL_PROJECTION
glMatrixMode(GL_PROJECTION)
# Carrega uma matriz identidade na matriz corrente
glLoadIdentity()
# Configurando os parâmetros para as fontes de luz
# GL_DIFFUSE define o parâmetro usado a luz difusa (no formato RGBA)
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1., 1., 1., 1.])
# Os três parâmetros definem a posição da fonte luminosa
# O quarto define se a fonte é direcional (0) ou posicional (1)
glLightfv(GL_LIGHT0, GL_POSITION, [-5., 5., -5., 1.])
# Aplica os parâmetros de iluminação
glEnable(GL_LIGHTING)
# Inclui a fonte de luz 0 no calculo da iluminação
glEnable(GL_LIGHT0)
# Inicia o laço de eventos da GLUT
glutMainLoop()