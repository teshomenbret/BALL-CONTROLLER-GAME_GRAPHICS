from model.cube import Cube


class Block(Cube):
    
    def __init__(self, position, size, color = (1, 0, 0, 0)):
        
        super().__init__(position, (size, 3, .5), color)
        self.speed = 0.015
        self.size = size


    # make the bloxk to move towards the z- asis
    def update(self, dt):
        x, y, z = self.position
        z += self.speed *dt
        self.position = x, y, z
    

    