from sphere import Sphere


class Player(Sphere):
    color = (0, 1, 0, 0)

    def __init__(self, radius, position, color):
        super().__init__(radius, position, color)
        self.score = 0
    
    def count(self):
        self.score = self.score+1
       
    


    
    