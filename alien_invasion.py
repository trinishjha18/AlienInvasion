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
        self.ship = Ship(self.screen)
        self.ship_speed = GameSettings.SHIP_SPEED.value
        
        # Movement flags for continuous movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        

    def run(self):
        while self.running:
            self.handle_events()
            self.update_ship()
            self.render_image()
            # flip() the display to put your work on screen
            pygame.display.flip()
            self.clock.tick(GameSettings.FPS.value)

    def handle_events(self):
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                if event.key == pygame.K_UP:
                    self.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.moving_left = False
                if event.key == pygame.K_UP:
                    self.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.moving_down = False
    
    def update_ship(self):
        # Update ship position based on movement flags and screen boundaries
        if self.moving_right and self.ship.image_rect.right < self.screen.get_rect().right:
            self.ship.image_rect.centerx += self.ship_speed
        if self.moving_left and self.ship.image_rect.left > 0:
            self.ship.image_rect.centerx -= self.ship_speed
        if self.moving_up and self.ship.image_rect.top > 0:
            self.ship.image_rect.centery -= self.ship_speed
        if self.moving_down and self.ship.image_rect.bottom < self.screen.get_rect().bottom:
            self.ship.image_rect.centery += self.ship_speed   

    def render_image(self):
        # Set screen to black
        self.screen.fill(Colors.BLACK.value)
        
        # Display image on the screen
        self.ship.blitme()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run()
    pygame.quit()
