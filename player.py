import pygame
from circleshape import CircleShape
from constants import *
from shots import Shots

class Player(CircleShape):
    def __init__(self, x, y, radius, shot_group):
        super().__init__(x, y, radius)
        self.rotation=0
        self.shot_group = shot_group
        self.shot_cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        tri_points = self.triangle()
        pygame.draw.polygon(screen, color="white", points=tri_points, width=2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED*dt)
    
    def update(self, dt):
        self.shot_cooldown-=dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown < 0:
                self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        shot = Shots(self.position.x, self.position.y, SHOT_RADIUS)
        velocity = pygame.Vector2(0,1)
        velocity = velocity.rotate(self.rotation)
        shot.velocity = velocity * PLAYER_SHOOT_SPEED
        self.shot_group.add(shot)
        
    