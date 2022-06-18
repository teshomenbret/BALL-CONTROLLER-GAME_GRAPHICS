from model.cube import Cube


class Builfing(Cube):
    
    def __init__(self, position, size,  color = (1, 1, 0, 0)):
        self.speed = 0.01
        super().__init__(position, size, color)
       
    
    def update(self, dt):
        
        x, y, z = self.position
        z += self.speed*dt
        self.position = x, y, z

    
    