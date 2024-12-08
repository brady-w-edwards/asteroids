import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')
        player1.draw(screen)
        player1.update(dt)

        # re-render display
        pygame.display.flip()
        
        # limit to 60 FPS
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()