import random
from model.block import Block
from model.building import Builfing
from model.cube import Cube
from model.grass import Grass
from model.player import Player
from model.texture import Texture



class Game:
    def __init__(self):
        self.game_over = False
        self.player =  Player(.6, position=(0, 0, 0),color=(0, 0, 1, 0))
        self.ground = Cube(position=(0, -1, -20),size=(16, 1, 122),color=(1, 1, 1, 1))
        self.grassLeft = Grass((-20, 0, -40), (25,0.1,80))
        self.grassRight = Grass((20, 0, -40), (25,0.1,80))
        self.blocks = []
        self.building = []
        self.texture = Texture()
        self.random_dt = 0
                

    def check_collisions(self):
        blocks = filter(lambda x: 0 < x.position[2] < 1,self.blocks)
        x = self.player.position[0]
        r = self.player.radius
        for block in blocks:
            x1 = block.position[0]
            s = block.size / 2
            if x1-s < x-r < x1+s or x1-s < x+r < x1+s:
                self.game_over = True
                print("Game over!")
                print(self.player.score)
                        

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
            if r < 0.01:
                self.random_dt = 0
                offset = random.choice([-13, 13])
                size =random.choice([(10,10,10), (6,6,6)])
                self.building.append(Builfing((offset, 0, -60), size))


    def generate_block(self, r):
        size = 7 if r < 0.03 else 6
        offset = random.choice([-4, 0, 4])
        self.blocks.append(Block((offset, 0, -70), size))


    def clear_past_blocks(self):
        blocks = filter(lambda x: x.position[2] > 5, self.blocks)
        for block in blocks:
            self.blocks.remove(block)
            del block
            self.player.count()
            

    def clear_past_building(self):
        buildings = filter(lambda x: x.position[2] > 5,
                        self.building)
        for building in buildings:
            self.building.remove(building)
            del building


    def display(self):
        self.grassRight.render(self.texture.grassTexture)
        self.grassLeft.render(self.texture.grassTexture)
        for block in self.blocks:
            block.render( self.texture.blockTexture)
        self.player.render()
        self.ground.render(self.texture.groundTexture)

        for building in self.building:
            building.render(self.texture.buildingTexture)


    def processInputLeft(self, dt):
        x, y, z = self.player.position
        x -= 0.01 * dt
        x = max(min(x, 6), -6)
        self.player.position = (x, y, z)


    def processInputRight(self, dt):
        x, y, z = self.player.position
        x += 0.01 * dt
        x = max(min(x, 6), -6)
        self.player.position = (x, y, z)

