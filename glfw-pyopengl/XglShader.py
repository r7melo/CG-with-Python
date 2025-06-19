from OpenGL.GL import *
from tools.load_file import load_file


def CompileShaderGPU(path_glsl, GL_TYPE_PIPELINE):
    x_shader_source = load_file(path_glsl)
    x_shader = glCreateShader(GL_TYPE_PIPELINE)
    glShaderSource(x_shader, x_shader_source)
    glCompileShader(x_shader)

    if not glGetShaderiv(x_shader, GL_COMPILE_STATUS):
        err = glGetShaderInfoLog(x_shader).decode()
        glDeleteShader(x_shader)
        raise RuntimeError(f"[{path_glsl}] Shader compilation failed: \n{err}")

    return x_shader