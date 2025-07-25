import pygame as pg
import constants as c
import circleshape as cs
import player as pl
import asteroid as ast
import asteroidfield as af
from shot import Shot

def main():
    pg.init()
    screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    player = pl.Player(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2)

    pg.time.Clock().tick(60)  # Set the frame rate to 60 FPS
    dt = 0.0  # Initialize delta time

    updatable_group = pg.sprite.Group()
    drawable_group = pg.sprite.Group()
    asteroid_group = pg.sprite.Group()
    shot_group = pg.sprite.Group()

    ast.Asteroid.containers = (updatable_group, drawable_group, asteroid_group)
    pl.containers = (updatable_group, drawable_group)
    af.AsteroidField.containers = (updatable_group)
    Shot.containers = (updatable_group, drawable_group, shot_group)

    updatable_group.add(player)
    drawable_group.add(player)

    asteroid_field = af.AsteroidField()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return

        fill_color = (0, 0, 0)  # Black background
        screen.fill(fill_color)

        updatable_group.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
        
        for sprite in drawable_group:
            sprite.draw(screen)

        pg.display.flip()
        dt = pg.time.Clock().tick(60) / 1000.0

    print("Starting Asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
