import sys
import pygame
from constants import *

def main():
    pygame.init()
    
    # delta time - time that has passed since the last frame was drawn
    deltaTime = 0
    FPS = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        screen.fill(BLACK)
        pygame.display.flip()
        deltaTime = FPS.tick(60) / 1000

if __name__ == "__main__":
    main()