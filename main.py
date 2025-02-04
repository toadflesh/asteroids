import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH,SCREEN_HEIGHT), 
        pygame.DOUBLEBUF | pygame.HWSURFACE
        )
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    delta_time = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,PLAYER_RADIUS,shot_group)
    asteroidfield = AsteroidField()
    print(f"Number of updateable sprites: {len(updateable)}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")

        updateable.update(delta_time)
        for item in drawable:
            item.draw(screen)
        
        shot_group.update(delta_time)
        for shot in shot_group:
            shot.draw(screen)

        for asteroid in asteroids:
            if asteroid.collisionCheck(player):
                print("Game Over!")
                exit(1)
            for shot in shot_group:
                if asteroid.collisionCheck(shot):
                    shot.kill()
                    asteroid.split()
               

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

if __name__=="__main__":
    main()