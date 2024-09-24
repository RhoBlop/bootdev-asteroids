import math
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers = None

    def __init__(self, x, y, radius):
        # we will be using this later
        if self.containers is not None:
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, window):
        # sub-classes must override
        pass

    def update(self, deltaTime):
        # sub-classes must override
        pass

    def is_colliding(self, circle):
        distance = self.position.distance_to(circle.position)
        return distance <= (self.radius + circle.radius)

    def __calculate_distance(coord1, coord2):
        return math.sqrt((coord1.x - coord2.x)**2 + (coord1.y - coord2.y)**2)