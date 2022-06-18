from cube import Cube
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Block(Cube):
    color = (1, 0, 0, 0)
    speed = 0.015
    
    def __init__(self, position, size):
        super().__init__(position, (size, 3, .5), Block.color)
        self.size = size

    def update(self, dt):
        x, y, z = self.position
        z += Block.speed *dt
        self.position = x, y, z
    

    def render(self,texture ):
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glTranslatef(*self.position)
        glMaterialfv(GL_FRONT, GL_DIFFUSE,self.color)
        for row in self.vertices:
            glBindTexture(GL_TEXTURE_2D,texture)
            glBegin(GL_QUADS)
            for v in Cube.sides:
                vvv =row[v]
                glTexCoord2f(vvv[3],vvv[4])
                glVertex3fv(vvv[:3])
            glEnd()
        glPopMatrix()