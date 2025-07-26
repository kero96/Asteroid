import pygame as pg
import circleshape as cs
import constants as c
import random

class Asteroid(cs.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0.0

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= c.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_radius = self.radius - c.ASTEROID_MIN_RADIUS
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = vel1 * 1.2
        asteroid2.velocity = vel2 * 1.2

        asteroid1.add(self.containers)
        asteroid2.add(self.containers)

