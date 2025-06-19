import glfw
from OpenGL.GL import *
import numpy as np
import math


def load_shader_file(path):
    with open(path, 'r') as file:
        return file.read()



def main():

    # Inicializar GLFW
    if not glfw.init():
        raise Exception("Falha ao incializar GLFW")


    # Configurar versão do OpenGL (3.3 Core Profile)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Criar a janela
    window = glfw.create_window(800,800, "Minha primeira janela OpenGL", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Falha ao criar janela")
 
    # Ativar contexto OpenGL
    glfw.make_context_current(window)

    # “Quero criar um shader para a etapa de processamento dos vértices.”
    vertex_shader_source = load_shader_file("./glfw-pyopengl/shaders/vertex_shader.glsl")
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, vertex_shader_source)
    glCompileShader(vertex_shader)

    # “Shader para processar os fragmentos (pixels) da imagem.”
    fragment_shader_source = load_shader_file("./glfw-pyopengl/shaders/fragment_shader.glsl")
    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, fragment_shader_source)
    glCompileShader(fragment_shader)

    shader_program = glCreateProgram() # cria um programa vazio
    glAttachShader(shader_program, vertex_shader)   # anexa o vertex shader
    glAttachShader(shader_program, fragment_shader)  # anexa o fragment shader
    glLinkProgram(shader_program)  # linka tudo no programa

    sucess = glGetProgramiv(shader_program, GL_LINK_STATUS)
    if not sucess:
        info_log = glGetProgramInfoLog(shader_program)
        raise Exception(f"Erro ao linkar shader program:\n{info_log.decode()}")
    
    vertices = np.array([
        # Primeiro triângulo (parte inferior)
        -0.5, -0.5,   # Vértice 0
        0.5, -0.5,   # Vértice 1
        -0.5,  0.5,   # Vértice 2

        # Segundo triângulo (parte superior)
        -0.5,  0.5,   # Vértice 2 (repetido)
        0.5, -0.5,   # Vértice 1 (repetido)
        0.5,  0.5,   # Vértice 3
    ], dtype=np.float32)


    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)
    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # "Esse VBO tem atributos de posição, com 2 floats por vértice, começando no índice 0":
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    scale_loc = glGetUniformLocation(shader_program, "scale")

    # Loop principal
    while not glfw.window_should_close(window):
        time = glfw.get_time()  # pega o tempo desde o início do programa em segundos
        scale_value =   math.sin(time)  # varia entre 0 e 1

        glClearColor(.1, .1, .1, 1) # Cor de fundo# Cor de fundo
        glClear(GL_COLOR_BUFFER_BIT) # Limpa a tela com a cor escolhida

        #region DRAW
        glUseProgram(shader_program)
        glUniform1f(scale_loc, scale_value)  # atualiza escala toda vez

        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 6)
        #endregion

        glfw.swap_buffers(window) # Troca os buffers (double buffering) 
        glfw.poll_events() # Processa eventos de teclado, mouse etc. 


    # Finalizar
    glfw.terminate()

if __name__ == "__main__":
    main()