import pygame as pg
import constants as c
import circleshape as cs
import player as pl

def main():
    pg.init()
    screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    player = pl.Player(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2)

    pg.time.Clock().tick(60)  # Set the frame rate to 60 FPS
    dt = 0.0  # Initialize delta time

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return

        fill_color = (0, 0, 0)  # Black background
        screen.fill(fill_color)

        player.draw(screen)
        player.update(dt)

        pg.display.flip()
        dt = pg.time.Clock().tick(60) / 1000.0

    print("Starting Asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
