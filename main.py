import pygame
import sys
from constants import *
from player import *
from shot import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # CREATE GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player1):
                sys.exit("Game over!")
            
            for bullet in shots:
                if bullet.collision(asteroid):
                    asteroid.split()

        screen.fill('black')
        
        for obj in drawable:
            obj.draw(screen)

        # re-render display
        pygame.display.flip()
        
        # limit to 60 FPS
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()