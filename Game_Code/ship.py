import pygame
from Game_Code.game_configs import GameConfigs

class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load("Images/Spaceship5.png")
        self.image = pygame.transform.scale(self.image, (GameConfigs.IMAGE_WIDTH.value, GameConfigs.IMAGE_HEIGHT.value))
        self.image_rect = self.image.get_rect()
        self.image_rect.bottom = self.screen_rect.bottom
        self.image_rect.centerx = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
