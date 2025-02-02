import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH,SCREEN_HEIGHT), 
        pygame.DOUBLEBUF | pygame.HWSURFACE
        )
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()

if __name__=="__main__":
    main()