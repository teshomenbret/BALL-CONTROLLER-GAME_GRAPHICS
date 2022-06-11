from openGLUtils import OpenGLUtils
import pygame
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os


class Box:
    def __init__(self, width=1, height=1, depth=1, color =[0, 1, 0, 1]): 
        sides = ((0,1,2,3), (3,2,7,6), (6,7,5,4),
             (4,5,1,0), (1,5,7,2), (4,0,3,6))
        p1 = [ width/2, -height/2, -depth/2]
        p2 = [ width/2,  height/2, -depth/2]
        p3 = [-width/2,  height/2, -depth/2]
        p4 = [-width/2, -height/2, -depth/2]
        p5 = [ width/2, -height/2,  depth/2]
        p6 = [ width/2,  height/2,  depth/2]
        p7 = [-width/2, -height/2,  depth/2]
        p8 = [-width/2,  height/2,  depth/2]

        # self.position = position
        self.color = color
        self.vertices  = np.array([
                        p1[0],p1[1],p1[2], self.color[0], self.color[1], self.color[2],
                        p2[0],p2[1],p2[2], self.color[0], self.color[1], self.color[2],
                        p3[0],p3[1],p3[2], self.color[0], self.color[1], self.color[2],
                        p4[0],p4[1],p4[2], self.color[0], self.color[1], self.color[2],
                        p5[0],p5[1],p5[2], self.color[0], self.color[1], self.color[2],
                        p6[0],p6[1],p6[2], self.color[0], self.color[1], self.color[2],
                        p7[0],p7[1],p7[2], self.color[0], self.color[1], self.color[2],
                        p8[0],p8[1],p8[2], self.color[0], self.color[1], self.color[2],
                         
                        ], dtype=np.float32)

       

    def render(self):
            programRef = OpenGLUtils.initializeProgram(
                OpenGLUtils.vertexShaderCode(), OpenGLUtils.fragmentShaderCode())


            vao = glGenVertexArrays(1)
            vbo = glGenBuffers(1)

            glBindBuffer(GL_ARRAY_BUFFER, vbo)

            glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
            glBindVertexArray(vao)

            positionLocation = glGetAttribLocation(programRef, "position")
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * self.vertices.itemsize, ctypes.c_void_p(0))
            glEnableVertexAttribArray(0)

            colorLocation = glGetAttribLocation(programRef, "color")
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE,6 * self.vertices.itemsize, ctypes.c_void_p(12))
            glEnableVertexAttribArray(1)


            # unbind VBO
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            # unbind VAO
            glBindVertexArray(0)

            glClear(GL_COLOR_BUFFER_BIT)

            glUseProgram(programRef)
            glBindVertexArray(vao)

            glDrawArrays(GL_TRIANGLES, 0, 6)
            
            glBindVertexArray(0)

