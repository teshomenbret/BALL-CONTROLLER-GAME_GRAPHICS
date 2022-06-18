from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Light(object):
   
    def __init__(self, light_id, position):
        self.light_id = light_id
        self.position = position
        self.current_color = 0
        self. colors = [
              (1.0,1.0,1.0,1.0),
              (1.0,0.5,0.5,1.0),
              (0.5,1.0,0.5,1.0),
              (0.5,0.5,1.,1.)]
        self. enabled = False

    def render(self):
        light_id = self.light_id
        color = self.colors[self.current_color]
        glLightfv(light_id, GL_POSITION, self.position)
        glLightfv(light_id, GL_DIFFUSE, color)
        glLightfv(light_id, GL_CONSTANT_ATTENUATION, 0.1)
        glLightfv(light_id, GL_LINEAR_ATTENUATION, 0.05)

    def switch_color(self):
        self.current_color += 1
        self.current_color %= len(self.colors)

    def enable(self):
        if not self.enabled:
            glEnable(GL_LIGHTING)
            self.enabled = True
        glEnable(self.light_id)