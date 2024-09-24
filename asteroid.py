import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, window):
        pygame.draw.circle(window, WHITE, (self.position.x, self.position.y), self.radius, DRAWING_LINE_WIDTH)

    def update(self, deltaTime):
        self.position += (self.velocity * deltaTime)