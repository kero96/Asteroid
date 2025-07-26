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

    score = 0
    lives = 3
    font = pg.font.Font(None, 36)

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
                lives -= 1
                asteroid.kill()
                if lives <= 0:
                    player.kill()
                    asteroid_group.empty()
                    shot_group.empty()
                    updatable_group.empty()
                    drawable_group.empty()

                    # DISPLAY GAME OVER MESSAGE
                    game_over_font = pg.font.Font(None, 120)
                    game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
                    text_rect = game_over_text.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2))
                    screen.blit(game_over_text, text_rect)
                    pg.display.flip()
                    pg.time.wait(2000)
                    pg.quit()
                    sys.exit()
                else:
                    player.position = pg.Vector2(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2)
                    break
                
        for asteroid in asteroid_group:
            for shot in shot_group:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    score += 10

        for sprite in drawable_group:
            sprite.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        pg.display.flip()
        dt = pg.time.Clock().tick(60) / 1000.0

    print("Starting Asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
