import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Sphere(object): 
    def __init__(self, radius, position, color):
        self.radius = radius
        self.position = position
        self.color = color
        self.quadratic = gluNewQuadric()
        self.slices =40
        self.stacks =40


    def render(self):
        random_number = random.randint(0, 90)
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glTranslatef(*self.position)
        glRotate(random_number, 1.0, 0.0, 0.0)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.color)
        gluQuadricTexture(self.quadratic, GL_TRUE)
        gluSphere(self.quadratic, self.radius, self.slices, self.stacks)
        glPopMatrix()