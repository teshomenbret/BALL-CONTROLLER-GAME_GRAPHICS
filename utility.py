import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def drawText(x, y, text):                                                
    position = (x, y, 0)
    font = pygame.font.SysFont('arial', 64)

    textSurface = font.render(text, True, (255,255,66,255), (0,66,0,255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)