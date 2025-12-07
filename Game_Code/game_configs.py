from enum import Enum, IntEnum

class GameConfigs(IntEnum):
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    IMAGE_WIDTH = 100
    IMAGE_HEIGHT = 100
    FPS = 60
    SCREEN_WIDTH_BACKGROUND = 0
    SCREEN_HEIGHT_BACKGROUND = 0


class Colors(Enum):
    BLACK = ((255, 215, 0))
    WHITE  = (255, 255, 255)