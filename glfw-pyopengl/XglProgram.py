from OpenGL.GL import *

def CreateProgramGPU(shaders=None):

    if shaders == None:
        shaders = []

    program = glCreateProgram()

    try:
        for shader in shaders:
          glAttachShader(program, shader)
        glLinkProgram(program)

        if not glGetProgramiv(program, GL_LINK_STATUS):
            err = glGetProgramInfoLog(program).decode()
            raise RuntimeError("")
        
        return program
    
    except Exception as e:
        glDeleteProgram(program)
        for shader in shaders:
            glDeleteShader(shader)
        raise e
    