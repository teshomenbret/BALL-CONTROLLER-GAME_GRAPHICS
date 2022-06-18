import os
import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from model.light import Light
from model.game import Game



class Window:
    def __init__(self, width = 700, height=600):

        self.title = 'Ball controller game'
        self.framePerSecond = 60
        self.width = width
        self.height = height
        self.light = Light(GL_LIGHT0, (0, 15, -2, 0))
        self.game = None
      

        
    def start(self):

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_mode((self.width, self.width),OPENGL | DOUBLEBUF)
        pygame.display.set_caption(self.title)
        # enable light
        self.light.enable()

        glEnable(GL_DEPTH_TEST)
        glClearColor(0, .1, 0, 1)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45,  self.width / self.height, 1, 100)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_CULL_FACE)
        self.game = Game()
        self.mainLoop()


    def mainLoop(self):

        # start the music
        clock = pygame.time.Clock()
        soundFolder = 'sound'
        music = pygame.mixer.music.load(os.path.join(soundFolder, 'Maleda.mp3'))
        pygame.mixer.music.play()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            gluLookAt(-1, 10, 10,
                        0, 0, -8,
                        0, 1, 0)
           
          
            self.light.render()
            self.game.display()
            if not self.game.gameOver:
                self.drawText(self.width-100, self.height-40, str(self.game.player.score))
                dt = clock.tick(self.framePerSecond)

                for block in self.game.blocks:
                    block.update(dt)
                for building in self.game.building:
                    building.update(dt)

                self.game.clearPastblocks()
                self.game.addRandomBlock(dt)
                self.game.generateBuilding(dt)
                self.game.checkCollisions()
                self.game.clearPastBuilding()

                # event or input to chenge the player postion
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]:
                    self.game.processInputLeft(dt)
                if pressed[pygame.K_RIGHT]:
                    self.game. processInputRight(dt)

            if  self.game.gameOver: 
                # stop the music
                pygame.mixer.music.stop()
                # leave meassage
                self.drawText(self.width/2-150, self.height/2 +150, "Game over")
                self.drawText(self.width/2-150, self.height/2+100, "Your score is: " + str(self.game.player.score)) 
                self.drawText(self.width/2-150, self.height/2, "close the window and type ") 
                self.drawText(self.width/2-150, self.height/2-40, "python  window.py to play again") 
                
            pygame.display.flip()
               

    def drawText(self,x, y, text): 
        
        font = pygame.font.SysFont('arial', 30)                                               
        textSurface = font.render(text, True, (255, 255, 66, 255), (0, 66, 0, 255))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glWindowPos2d(x, y)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

                

def main():
    window = Window()
    window.start()


main()