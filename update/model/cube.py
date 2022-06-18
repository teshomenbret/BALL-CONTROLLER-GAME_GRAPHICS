from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *



class Cube(object):
    sides = (0,1,2,3)
    
    def __init__(self, position, size, color):
        self.position = position
        self.color = color
        x, y, z = map(lambda i: i/2, size)
        
        # we need 24 face for the texture to be exact
        self.vertices = [
                    [
                        [-x, -y,  z,  0.0, 0.0],
                        [x, -y,  z,     1.0, 0.0,],
                        [x,  y,  z,    1.0, 1.0,],
                        [-x,  y,  z,   0.0, 1.0,]
                    ],

                    [
                        [-x, -y, -z,   0.0, 0.0,],
                        [x, -y, -z,    1.0, 0.0,],
                        [x,  y, -z,     1.0, 1.0,],
                        [-x,  y, -z,   0.0, 1.0,],
                    ],

                    [
                       [ x, -y, -z,   0.0, 0.0,],
                        [x,  y, -z,   1.0, 0.0,],
                        [x,  y,  z,    1.0, 1.0,],
                        [x, -y,  z,    0.0, 1.0,],
                    ],

                    [
                        [-x,  y, -z,   0.0, 0.0,],
                        [-x, -y, -z,   1.0, 0.0,],
                        [-x, -y,  z,   1.0, 1.0,],
                        [-x,  y,  z,   0.0, 1.0,],

                    ],

                    [
                        [-x, -y, -z,   0.0, 0.0,],
                        [x, -y, -z,    1.0, 0.0,],
                        [x, -y,  z,    1.0, 1.0,],
                        [-x, -y,  z,    0.0, 1.0,],
                    ],

                    [
                        [  x,  y, -z,    0.0, 0.0,],
                        [ -x,  y, -z,    1.0, 0.0,],
                        [-x,  y,  z,     1.0, 1.0, ],
                        [x,  y,  z,      0.0, 1.0 ]  ,
                    
                    ]
                    
                    ]


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


        