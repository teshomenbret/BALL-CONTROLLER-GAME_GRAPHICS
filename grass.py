from cube import Cube


class Grass(Cube):
    color = (0, 1, 0, 0)

    def __init__(self, position, size):
        super().__init__(position, size, Grass.color)
       
    


    
    