import pygame
from Game_code.game_enums import *

class Ship():
    def __init__(self, screen):
        self.screen = screen
        # Load image on the screen
        # FIXME: Find background free files for this project.
        self.image = pygame.image.load("Images/Spaceship5.png")

        # Resize any image
        self.image = pygame.transform.scale(
            self.image, (GameSettings.IMAGE_WIDTH.value, GameSettings.IMAGE_HEIGHT.value))

        # Get coordinates of image
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Align image and screen together
        self.image_rect.bottom = self.screen_rect.bottom
        self.image_rect.centerx = self.screen_rect.centerx
        
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)