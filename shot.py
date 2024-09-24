import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, window):
        pygame.draw.circle(window, WHITE, self.position, self.radius, DRAWING_LINE_WIDTH)

    def update(self, deltaTime):
        self.position += (self.velocity * deltaTime)