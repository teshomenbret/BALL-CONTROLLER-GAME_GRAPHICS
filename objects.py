from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import * 

class Cube(object):
    sides = (
        (0,1,2,3), (3,2,7,6),
        (6,7,5,4),(4,5,1,0), 
        (1,5,7,2),(4,0,3,6)
    )

    def __init__(self, position, size,color):
        self.position = position
        self.color = color
        x, y, z = map(lambda i: i/2, size)
        self.vertices = (
                (x, -y, -z), (x, y, -z),
                (-x, y, -z), (-x, -y, -z),
                (x, -y, z), (x, y, z),
                (-x, -y, z), (-x, y, z)
            )

    def render(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glEnable(GL_LIGHTING)
        glEnable(GL_CULL_FACE)

        glBegin(GL_QUADS)
        glMaterialfv(GL_FRONT, GL_DIFFUSE,self.color)
        for side in Cube.sides:
            for v in side:
                glVertex3fv(self.vertices[v])
        glEnd()
        glPopMatrix()



class Light(object):
    enabled = False
    colors = [
        (1.,1.,1.,1.),
        (1.,0.5,0.5,1.),
        (0.5,1.,0.5,1.),
        (0.5,0.5,1.,1.)
    ]
    def __init__(self, light_id,position):
        self.light_id = light_id
        self.position = position
        self.current_color = 0


    def render(self):
        light_id = self.light_id
        color = Light.colors[self.current_color]
        glLightfv(light_id, GL_POSITION,self.position)
        glLightfv(light_id, GL_DIFFUSE,color)
        glLightfv(light_id,GL_CONSTANT_ATTENUATION, 0.1)
        glLightfv(light_id,GL_LINEAR_ATTENUATION, 0.05)


    def switch_color(self):
        self.current_color += 1
        self.current_color %= len(Light.colors)


    def enable(self):
        if not Light.enabled:
            glEnable(GL_LIGHTING)
            Light.enabled = True

        glEnable(self.light_id)

    
class Sphere(object):
    slices = 40
    stacks = 40


    def __init__(self, radius, position,color):
        self.radius = radius
        self.position = position
        self.color = color
        self.quadratic = gluNewQuadric()



    def render(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glMaterialfv(GL_FRONT, GL_DIFFUSE,
        self.color)
        # glutSolidSphere(self.radius,Sphere.slices, Sphere.stacks)
        gluSphere(self.quadratic,self.radius,Sphere.slices,Sphere.stacks)

        glPopMatrix()


class Block(Cube):
    color = (0, 0, 1, 1)
    speed = 0.01

    def __init__(self, position, size):
        super().__init__(position, (size,1, 1), Block.color)
        self.size = size

    def update(self, dt):
        x, y, z = self.position
        z += Block.speed * dt
        self.position = x, y, z


