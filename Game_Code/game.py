import pygame
from Game_Code.game_configs import GameConfigs, Colors
from Game_Code.ship import Ship
from Game_Code.input_handler import InputHandler


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
            
            # Blit the ship image
            self.ship.blitme()

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(GameConfigs.FPS.value)  # limits FPS to 60

    def update_ship(self):
        if self.handle_events.moving_right and self.ship.image_rect.right < self.screen.get_rect().right:
            self.ship.image_rect.centerx += self.ship_speed
        if self.handle_events.moving_left and self.ship.image_rect.left > 0:
            self.ship.image_rect.centerx -= self.ship_speed
        if self.handle_events.moving_up and self.ship.image_rect.top > 0:
            self.ship.image_rect.centery -= self.ship_speed
        if self.handle_events.moving_down and self.ship.image_rect.bottom < self.screen.get_rect().bottom:
            self.ship.image_rect.centery += self.ship_speed 
