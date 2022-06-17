import os
import sys
import random
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from block import Block
from building import Builfing
from cube import Cube
from light import Light
from sphere import Sphere



class App(object):
    def __init__(self, width = 700, height=600):
        self.title = 'ball controller game'
        self.fps = 60
        self.width = width
        self.height = height
        self.game_over = False

        self.random_dt = 0

        self.blocks = []
        self.building = []

        self.light = Light(GL_LIGHT0, (0, 15, -25, 1))
        self.player = Sphere(.6, position=(0, 0, 0),
                             color=(0, 1, 0, 1))
        self.ground = Cube(position=(0, -1, -20),
                           size=(16, 1, 110),
                           color=(1, 1, 1, 1))

        
    def start(self):
        pygame.init()
        pygame.mixer.init()

        pygame.display.set_mode((self.width, self.width),OPENGL | DOUBLEBUF)
        pygame.display.set_caption(self.title)
        self.light.enable()
        glEnable(GL_DEPTH_TEST)
        glClearColor(0, .6, 0, 1)
        glMatrixMode(GL_PROJECTION)
        aspect = self.width / self.height
        gluPerspective(45, aspect, 1, 100)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_CULL_FACE)

        self.main_loop()

    def main_loop(self):
        clock = pygame.time.Clock()
        s = 'sound'
        music = pygame.mixer.music.load(os.path.join(s, 'Maleda.mp3'))
        pygame.mixer.music.play(-1)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if not self.game_over:
                self.display()
                dt = clock.tick(self.fps)
                for block in self.blocks:
                    block.update(dt)
                for building in self.building:
                    building.update(dt)

                self.clear_past_blocks()
                self.add_random_block(dt)
                self.generate_building(dt)
                self.check_collisions()
                self. clear_past_building()
                self.process_input(dt)
                

    def check_collisions(self):
        blocks = filter(lambda x: 0 < x.position[2] < 1,
                        self.blocks)
        x = self.player.position[0]
        r = self.player.radius
        for block in blocks:
            x1 = block.position[0]
            s = block.size / 2
            if x1-s < x-r < x1+s or x1-s < x+r < x1+s:
                self.game_over = True
                print("Game over!")
                

    def add_random_block(self, dt):
        self.random_dt += dt
        if self.random_dt >= 900:
            r = random.random()
            if r < 0.055:
                self.random_dt = 0
                self.generate_block(r)
                

            
    def generate_building(self, dt):
        self.random_dt += dt
        if self.random_dt >= 800:
            r = random.random()
            if r < 0.02:
                self.random_dt = 0
                # size = (10,10,10)
                offset = random.choice([-13, 13])
                size =random.choice([(10,10,10), (6,6,6)])
                self.building.append(Builfing((offset, 0, -40), size))


    def generate_block(self, r):
        size = 7 if r < 0.03 else 6
        offset = random.choice([-4, 0, 4])
        self.blocks.append(Block((offset, 0, -60), size))


    def clear_past_blocks(self):
        blocks = filter(lambda x: x.position[2] > 5,
                        self.blocks)
        for block in blocks:
            self.blocks.remove(block)
            del block

    def clear_past_building(self):
        buildings = filter(lambda x: x.position[2] > 5,
                        self.building)
        for building in buildings:
            self.building.remove(building)
            del building
        


    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(-1, 10, 10,
                  0, 0, -8,
                  0, 1, 0)
        self.light.render()

        
        for block in self.blocks:
            block.render( )
        self.player.render()
        self.ground.render()
        

        for building in self.building:
            building.render()
        
        
        
        pygame.display.flip()

    def process_input(self, dt):
        pressed = pygame.key.get_pressed()
        x, y, z = self.player.position
        if pressed[K_LEFT]:
            x -= 0.01 * dt
        if pressed[K_RIGHT]:
            x += 0.01 * dt
        x = max(min(x, 6), -6)
        self.player.position = (x, y, z)


def main():
    app = App()
    app.start()


main()