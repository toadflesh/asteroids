import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            color="white", 
            center=(self.position.x, self.position.y), 
            radius=self.radius, 
            width=2 )
    
    def update(self, dt):
        self.position+=(self.velocity*dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_v1 = self.velocity.rotate(angle)
        new_v2 = self.velocity.rotate(-angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position.x,self.position.y,new_rad)
        new_ast2 = Asteroid(self.position.x,self.position.y,new_rad)

        new_ast1.velocity = new_v1*1.2
        new_ast2.velocity = new_v2*1.2

        

