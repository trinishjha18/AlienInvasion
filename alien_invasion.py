import pygame
from Game_Code.game_configs import GameConfigs
from Game_Code.ship import *


class AlienInvasion:
    def __init__(self):
        # pygame setup
        pygame.init()

    def run(self):
        screen = pygame.display.set_mode((GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))
        clock = pygame.time.Clock()
        running = True
        background_image = pygame.image.load("Images/Background2.png").convert()
        background_image = pygame.transform.scale(background_image, (GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Blit the background image
            screen.blit(background_image, (GameConfigs.SCREEN_WIDTH_BACKGROUND.value, GameConfigs.SCREEN_HEIGHT_BACKGROUND.value))

            ship = Ship(screen)
            ship.blitme()


            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(GameConfigs.FPS.value)  # limits FPS to 60

        pygame.quit()


def main():
    alien_invasion = AlienInvasion()
    alien_invasion.run()

if __name__ == "__main__":
    main()