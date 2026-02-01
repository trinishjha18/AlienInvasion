import pygame
from enum import Enum, IntEnum

class GameConfigs(IntEnum):
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    IMAGE_WIDTH = 100
    IMAGE_HEIGHT = 100
    FPS = 60
    SCREEN_WIDTH_BACKGROUND = 0
    SCREEN_HEIGHT_BACKGROUND = 0
    SHIP_SPEED = 5


class Colors(Enum):
    BLACK = (0, 0, 0)
    WHITE  = (255, 255, 255)


class Backgrounds:
    def __init__(self):
        self.screen1 =  pygame.image.load("Images/Background2.png").convert()
        self.level1_screen = pygame.transform.scale(self.screen1, (GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))
        self.screen2 = pygame.image.load("Images/menu_screen_bg3.jpg").convert()
        self.menu_screen = pygame.transform.scale(self.screen2, (GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))
        self.screen3 = pygame.image.load("Images/pause_screen_bg.jpg").convert()
        self.pause_screen = pygame.transform.scale(self.screen3, (GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))

