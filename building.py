from block import Block
from cube import Cube

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Builfing(Cube):
    speed = 0.01
    
    def __init__(self, position, size,  color = (1, 1, 0, 0)):
        super().__init__(position, size, color)
       
    
    def update(self, dt):
        x, y, z = self.position
        z += Builfing.speed *dt
        self.position = x, y, z

    
    