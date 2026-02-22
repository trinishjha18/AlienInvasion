import pygame
from Game_Code.game_configs import Colors

class HUD:
    def __init__(self, screen, score_system):
        self.screen = screen
        self.score_system = score_system
        
        self.font = pygame.font.SysFont(None, 36)
        
    def draw(self):
        score_text = f"Score: {self.score_system.score}"
        text_surface = self.font.render(score_text, True, Colors.WHITE.value)
        self.screen.blit(text_surface, (20, 20))