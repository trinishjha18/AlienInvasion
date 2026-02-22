import pygame
from Game_Code.game_configs import GameConfigs


class Alien:
    def __init__(self, screen, x, y, level):
        self.screen = screen
        
        if level % 2 != 0:
            image_path = "Images/Alien.png"
        else:
            image_path = "Images/Alien2.png"

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (GameConfigs.IMAGE_WIDTH, GameConfigs.IMAGE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        self.screen.blit(self.image, self.rect)