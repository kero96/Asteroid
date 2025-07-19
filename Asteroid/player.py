import pygame
import circleshape as cs
import constants as c

class Player(cs.CircleShape):
    def __init__(self, x , y):
        super().__init__(x, y, c.PLAYER_RADIUS)
        self.rotation = 0.0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)

    def rotate(self, dt):
        self.rotation += c.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt)


    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * c.PLAYER_SPEED * dt
        elif keys[pygame.K_s]:
            backward = pygame.Vector2(0, -1).rotate(self.rotation)
            self.position += backward * c.PLAYER_SPEED * dt

        # Wrap around the screen
        self.position.x %= c.SCREEN_WIDTH
        self.position.y %= c.SCREEN_HEIGHT