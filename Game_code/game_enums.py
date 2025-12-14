from enum import Enum, IntEnum

class Colors(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


class GameSettings(IntEnum):
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    IMAGE_WIDTH = 100
    IMAGE_HEIGHT = 100
    FPS = 60
    SHIP_SPEED = 5
