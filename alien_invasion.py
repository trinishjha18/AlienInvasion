import pygame
from Game_code.game_enums import *

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConfig.SCREEN_WIDTH.value, GameConfig.SCREEN_HEIGHT.value))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.render_image()
            # flip() the display to put your work on screen
            pygame.display.flip()
            self.clock.tick(GameConfig.FPS.value)
            
    def handle_events(self):
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def render_image(self):
        # Load image on the screen
            # FIXME: Find background free files for this project.
            image = pygame.image.load("Images/Spaceship5.png")
            
            # Resize any image
            image = pygame.transform.scale(image, (GameConfig.IMAGE_WIDTH.value, GameConfig.IMAGE_HEIGHT.value))
            
            # Get coordinates of image
            image_rect = image.get_rect()
            screen_rect = self.screen.get_rect()
            
            # Align image and screen together
            image_rect.bottom = screen_rect.bottom
            image_rect.centerx = screen_rect.centerx

            # Display image on the screen
            self.screen.blit(image, image_rect)

if __name__ == "__main__":
    game = AlienInvasion()
    game.run()
    pygame.quit()