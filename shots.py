import pygame
from circleshape import CircleShape
from constants import *

class Shots(CircleShape):
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

    