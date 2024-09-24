import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, window):
        pygame.draw.circle(window, WHITE, self.position, self.radius, DRAWING_LINE_WIDTH)

    def update(self, deltaTime):
        self.position += (self.velocity * deltaTime)

    def split(self):
        # removes current asteroid in all cases
        self.kill()

        # this is the smallest asteroid, so there's no splitting
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        rand_angle = random.uniform(20, 50)
        velocity_ast1, velocity_ast2 = self.velocity.rotate(rand_angle), self.velocity.rotate(-rand_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        ast1, ast2 = Asteroid(self.position.x, self.position.y, radius), Asteroid(self.position.x, self.position.y, radius)

        ast1.velocity = velocity_ast1 * 1.2
        ast2.velocity = velocity_ast2 * 1.2