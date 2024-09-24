import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    def draw(self, window):
        pygame.draw.polygon(window, WHITE, self.triangle(), DRAWING_LINE_WIDTH)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius # type: ignore
        b = self.position - forward * self.radius - right # type: ignore
        c = self.position - forward * self.radius + right # type: ignore
        return [a, b, c]

    def update(self, deltaTime):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.rotate(deltaTime)
        if keys[pygame.K_a]:
            self.rotate(-deltaTime)
        if keys[pygame.K_w]:
            self.move(deltaTime)
        if keys[pygame.K_s]:
            self.move(-deltaTime)

    def move(self, deltaTime):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * deltaTime

    def rotate(self, deltaTime):
        self.rotation += PLAYER_TURN_SPEED * deltaTime
    