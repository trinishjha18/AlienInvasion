import pygame

from Game_Code.game_configs import Colors


class Bullet:
    def __init__(self, screen, position):
        self.screen = screen

        self.rect = pygame.Rect(0, 0, 4, 15)
        self.rect.centerx = position.centerx
        self.rect.top = position.top

        self.color = Colors.WHITE.value

        self.speed = 10

    def move(self):
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def is_off_screen(self):
        return self.rect.bottom < 0