import glfw
from OpenGL.GL import *
import numpy as np
import math
import time
import threading
from XglShader import *
from XglProgram import *

#region GLOBAIS
WINDOWS_TITLE = "Minha primeira janela OpenGL"
WINDOWS_SIZE = (800, 800)
TARGET_FPS = 60
#endregion




def render_loop(window):
    # Ativar contexto OpenGL
    glfw.make_context_current(window)

    vertex_shader = CompileShaderGPU("./glfw-pyopengl/shaders/vertex_shader.glsl", GL_VERTEX_SHADER)
    fragment_shader = CompileShaderGPU("./glfw-pyopengl/shaders/fragment_shader.glsl", GL_FRAGMENT_SHADER)
    shader_program = CreateProgramGPU([vertex_shader, fragment_shader])

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

    frame_duration = 1.0 / TARGET_FPS
    last_time = glfw.get_time()

    while not glfw.window_should_close(window):
        current_time = glfw.get_time()
        elapsed = current_time - last_time
        if elapsed >= frame_duration:
            last_time = current_time
            # roda a renderização
            
            scale = (1 + math.sin(current_time)) / 2

            glClearColor(0.1, 0.1, 0.1, 1)
            glClear(GL_COLOR_BUFFER_BIT)

            glUseProgram(shader_program)
            glUniform1f(scale_loc, scale)

            glBindVertexArray(VAO)
            glDrawArrays(GL_TRIANGLES, 0, 6)

            glfw.swap_buffers(window)

        else:
            time.sleep(frame_duration - elapsed)


def framebuffer_size_callback(window, width, height):
    glViewport(0, 0, width, height)


def main():

    # Inicializar GLFW
    if not glfw.init():
        raise Exception("Falha ao incializar GLFW")

    # Configurar versão do OpenGL (3.3 Core Profile)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Criar a janela
    window = glfw.create_window(WINDOWS_SIZE[0],WINDOWS_SIZE[1], WINDOWS_TITLE, None, None)
    if not window:
        glfw.terminate()
        raise Exception("Falha ao criar janela")

    render_thread = threading.Thread(target=render_loop, args=(window,))
    render_thread.start()

    # Loop de eventos]
    while not glfw.window_should_close(window):
        glfw.poll_events()
        time.sleep(1/100)

    

    # Finalizar
    glfw.terminate()


if __name__=="__main__":
    main()