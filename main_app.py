import math
import random
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

from objects import   Block, Cube, Light, Sphere 


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

    
    def process_input(self, dt):
        pressed = pygame.key.get_pressed()
        x, y, z = self.player.position
        if pressed[K_LEFT]:
            x -= 0.01 * dt
        if pressed[K_RIGHT]:
            x += 0.01 * dt
        x = max(min(x, 7), -7)
        self.player.position = (x, y, z)

    
    def check_collisions(self):
        blocks = filter(lambda x: 0 <x.position[2] < 1,self.blocks)
        x = self.player.position[0]
        r = self.player.radius
        for block in blocks:        
            x1 = block.position[0]
            s = block.size / 2
            if x1-s < x-r < x1+s or x1-s <x+r < x1+s:
                self.game_over = True
                print("Game over!")

        
    def add_random_block(self, dt):
        self.random_dt += dt
        if self.random_dt >= 800:
            r = random.random()
            if r < 0.1:
                self.random_dt = 0
                self.generate_block(r)


    def generate_block(self, r):
        size = 7 if r < 0.03 else 5
        offset = random.choice([-4, 0, 4])
        self.blocks.append(Block((offset,0, -40), size))

    
    def clear_past_blocks(self):
        blocks = filter(lambda x:x.position[2] > 5,self.blocks)
        for block in blocks:
            self.blocks.remove(block)
            del block


    def display(self):
        # glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)
        # glLoadIdentity()
        # gluLookAt(0, 10, 10,0, 0, -5,0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)
        x = math.sin(self.angle) *self.distance
        z = math.cos(self.angle) *self.distance
        glLoadIdentity()
        gluLookAt(x, 0, z,0, 0, 0,0, 1, 0)
        self.light.render()
        for block in self.blocks:
            block.render()
        self.player.render()
        self.ground.render()
        pygame.display.flip()

        # x = math.sin(self.angle) *self.distance
        # z = math.cos(self.angle) *self.distance
        # glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)
        # glLoadIdentity()
        # gluLookAt(x, 0, z,0, 0, 0,0, 1, 0)
        # self.light.render()
        # self.sphere1.render()
        # self.sphere2.render()
        # pygame.display.flip()


    def quit(self):
        pygame.quit()
        sys.exit()