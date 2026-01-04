import pygame
from Game_Code.game_configs import GameConfigs
from Game_Code.ship import Ship
from Game_Code.input_handler import InputHandler
from Game_Code.ship_controller import ShipController


class AlienInvasion:
    def __init__(self):
        # pygame setup
        pygame.init()

        self.screen = pygame.display.set_mode((GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))
        self.clock = pygame.time.Clock()
        
        self.running = True
        
        self.ship = Ship(self.screen)
        self.ship_speed = GameConfigs.SHIP_SPEED.value

        self.handle_events = InputHandler()
        self.ship_controller = ShipController(self.handle_events, self.ship, self.screen, self.ship_speed)


    def run(self):
        while self.running:
            self.running = self.handle_events.process_events()
            self.update_ship()
            self.display_settings(self.render_image())
        pygame.quit()

    def render_image(self):
        background_image = pygame.image.load("Images/Background2.png").convert()
        background_image = pygame.transform.scale(background_image, (GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))
        return background_image
    
    def display_settings(self, background_image):
        # Blit the background image
            self.screen.blit(background_image, (GameConfigs.SCREEN_WIDTH_BACKGROUND.value, GameConfigs.SCREEN_HEIGHT_BACKGROUND.value))
            
            self.ship.blitme()

            pygame.display.flip()

            self.clock.tick(GameConfigs.FPS.value)

    def update_ship(self):
        self.ship_controller.update_ship()