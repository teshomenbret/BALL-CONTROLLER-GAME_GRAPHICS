from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

from objects import   Cube, Light, Sphere 


class App(object):
    def init(self, width=800,height=600):
        # self.light = Light(GL_LIGHT0, (15,5, 15, 1))
        # self.sphere1 = Sphere(2, (0, 0,0), (1, 1, 1, 1))
        # self.sphere2 = Sphere(1, (4, 2,0), (1, 0.4, 0.4, 1))

        self.game_over = False
        self.random_dt = 0
        self.blocks = []
        self.light = Light(GL_LIGHT0, (0,15, -25, 1))
        self.player = Sphere(1, position=(0, 0, 0),color=(0, 1,0, 1))
        self.ground = Cube(position=(0,-1, -20),size=(16, 1,60),color=(1, 1, 1,1))


        self.title = 'OpenGL demo'
        self.fps = 60

        self.width = width
        self.height = height
        self.angle = 0
        self.distance = 20


    def start(self):
        pygame.init()
        pygame.display.set_mode((self.width,self.height),OPENGL |DOUBLEBUF)
        pygame.display.set_caption(self.title)

        glEnable(GL_CULL_FACE)

        glEnable(GL_DEPTH_TEST)
        self.light.enable()
        glEnable(GL_LIGHT0)
        glClearColor(.1, .1, .1, 1)

        aspect = self.width / self.height
        gluPerspective(40., aspect, 1.,40.)
        glMatrixMode(GL_MODELVIEW)
        self.main_loop()