import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # objects groups
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    Player.containers = (drawable_group, updatable_group)
    Asteroid.containers = (asteroids_group, drawable_group, updatable_group)
    AsteroidField.containers = (updatable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids_field = AsteroidField()
    # delta time - time that has passed since the last frame was drawn
    deltaTime = 0

    print("Starting asteroids!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        window.fill(BLACK)
        
        for obj in updatable_group:
            obj.update(deltaTime)
        for obj in drawable_group:
            obj.draw(window)
        for asteroid in asteroids_group:
            if player.is_colliding(asteroid):
                print("Game Over!")
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        # limit framerate
        deltaTime = clock.tick(FRAMERATE) / 1000

if __name__ == "__main__":
    main()