import pygame
from Game_Code.game_configs import GameConfigs, Colors
from Game_Code.ship import *


class AlienInvasion:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))
        self.clock = pygame.time.Clock()
        self.running = True
        self.ship = Ship(self.screen)


    def run(self):
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_settings(self.render_image())
            
        pygame.quit()


    def render_image(self):
        background_image = pygame.image.load("Images/Background2.png").convert()
        background_image = pygame.transform.scale(background_image, (GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))
        return background_image


    def display_settings(self, background_image):
        # Blit the background image
            self.screen.blit(background_image, (GameConfigs.SCREEN_WIDTH_BACKGROUND.value, GameConfigs.SCREEN_HEIGHT_BACKGROUND.value))
            
            # Blit the ship image
            self.ship.blitme()

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(GameConfigs.FPS.value)  # limits FPS to 60




def main():
    alien_invasion = AlienInvasion()
    alien_invasion.run()

if __name__ == "__main__":
    main()