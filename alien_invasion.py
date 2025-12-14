import pygame
from Game_Code.game_configs import GameConfigs, Colors
from Game_Code.ship import Ship


class AlienInvasion:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))
        self.clock = pygame.time.Clock()
        self.running = True
        self.ship = Ship(self.screen)
        self.ship_speed = GameConfigs.SHIP_SPEED.value

        # Make sure ship is not continuosly moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def run(self):
        while self.running:
            self.handle_events()
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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the user closes the window running is off
                self.running = False
            elif event.type == pygame.KEYDOWN:
                # If right key is pressed move to the right
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                # If left key is pressed move to the left
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                # If up key is pressed move to the up
                if event.key == pygame.K_UP:
                    self.moving_up = True
                # If down key is pressed move to the down
                if event.key == pygame.K_DOWN:
                    self.moving_down = True
            elif event.type == pygame.KEYUP:
                # If the right key is not pressed don't move right
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                # If the left key is not pressed don't move left
                if event.key == pygame.K_LEFT:
                    self.moving_left = False
                # If the up key is not pressed don't move up
                if event.key == pygame.K_UP:
                    self.moving_up = False
                # If the down key is not pressed don't move down
                if event.key == pygame.K_DOWN:
                    self.moving_down = False


    def update_ship(self):
        if self.moving_right and self.ship.image_rect.right < self.screen.get_rect().right:
            self.ship.image_rect.centerx += self.ship_speed
        if self.moving_left and self.ship.image_rect.left > 0:
            self.ship.image_rect.centerx -= self.ship_speed
        if self.moving_up and self.ship.image_rect.top > 0:
            self.ship.image_rect.centery -= self.ship_speed
        if self.moving_down and self.ship.image_rect.bottom < self.screen.get_rect().bottom:
            self.ship.image_rect.centery += self.ship_speed 




def main():
    alien_invasion = AlienInvasion()
    alien_invasion.run()

if __name__ == "__main__":
    main()