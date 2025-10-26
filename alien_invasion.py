import pygame
from Game_code.game_enums import *
from Game_code.ship import *


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (GameSettings.SCREEN_WIDTH.value, GameSettings.SCREEN_HEIGHT.value))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.render_image()
            # flip() the display to put your work on screen
            pygame.display.flip()
            self.clock.tick(GameSettings.FPS.value)

    def handle_events(self):
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render_image(self):
        # Set screen to black
        self.screen.fill(Colors.BLACK.value)
        ship = Ship(self.screen)
        # Display image on the screen
        ship.blitme()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run()
    pygame.quit()
