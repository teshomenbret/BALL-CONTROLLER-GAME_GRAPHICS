import os
from OpenGL.GL import *
class OpenGLUtils(object):
    @staticmethod
    def initializeShader(shaderCode, shaderType):
        shaderCode = shaderCode
        shaderRef = glCreateShader(shaderType)
        glShaderSource(shaderRef, shaderCode)
        glCompileShader(shaderRef)
        return shaderRef 
    

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)
        programRef = glCreateProgram()
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)
        glLinkProgram(programRef)
        return programRef

    @staticmethod
    def getFileContents(filename):
        p = os.path.join(os.getcwd(), "shaders", filename)
        return open(p, 'r').read()


# make those method to reade from the file
    @staticmethod
    def vertexShaderCode():
        return  OpenGLUtils.getFileContents("triangle.vertex.shader")

    @staticmethod
    def fragmentShaderCode():
        return OpenGLUtils.getFileContents("triangle.fragment.shader")


    