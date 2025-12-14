import pygame
from Game_code.game_enums import Colors, GameSettings
from Game_code.ship import Ship
from Game_code.input_handler import InputHandler
from Game_code.ship_controller import ShipController


class AlienInvasion:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(
            (GameSettings.SCREEN_WIDTH.value, GameSettings.SCREEN_HEIGHT.value))
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.ship = Ship(self.screen)
        self.ship_speed = GameSettings.SHIP_SPEED.value
        
        self.input_handler = InputHandler()
        self.ship_controller = ShipController(self.input_handler, self.screen, self.ship, self.ship_speed)
        
        
    def run(self):
        while self.running:
            self.running = self.input_handler.process_events()
            self.ship_controller.update_ship()
            self.render()
            self.clock.tick(GameSettings.FPS.value)
    
    def render(self):
        # Set screen to black
        self.screen.fill(Colors.BLACK.value)
        # Display image on the screen
        self.ship.blitme()
        # flip() the display to put your work on screen
        pygame.display.flip()