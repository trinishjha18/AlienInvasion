import pygame
from Game_Code.game_configs import Colors


class HUD:
    def __init__(self, screen, score_system, level_system):
        self.screen = screen
        self.score_system = score_system
        self.level_system = level_system

        self.font = pygame.font.SysFont(None, 36)

    # def update(self, level_system):
    #     self.level = level

    def draw(self):
        score_text = f"Score: {self.score_system.score}"
        level_text = f"Level: {self.level_system.level}"

        display_score_text = self.font.render(score_text, True, Colors.WHITE.value)
        display_level_text = self.font.render(level_text, True, Colors.WHITE.value)

        self.screen.blit(display_score_text, (20, 20))
        self.screen.blit(display_level_text, (20, 60))