import pygame
from Game_Code.game_configs import GameConfigs


class Alien:
    def __init__(self, screen, x, y):
        self.screen = screen

        self.image = pygame.image.load("Images/Alien.png")
        self.image = pygame.transform.scale(self.image, (GameConfigs.IMAGE_WIDTH, GameConfigs.IMAGE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        self.screen.blit(self.image, self.rect)