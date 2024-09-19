import sys
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # delta time - time that has passed since the last frame was drawn
    deltaTime = 0

    print("Starting asteroids!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        window.fill(BLACK)
        player.update(deltaTime)

        player.draw(window)
        pygame.display.flip()

        # limit framerate
        deltaTime = clock.tick(FRAMERATE) / 1000

if __name__ == "__main__":
    main()