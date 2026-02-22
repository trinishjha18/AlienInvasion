from Game_Code.game_configs import Colors
import pygame

class HUD:
    def __init__(self, screen, score_system, level_system):
        self.screen = screen
        self.score_system = score_system
        self.level_system = level_system
        
        self.font = pygame.font.SysFont(None, 36)
        
    def draw(self):
        score_text = f"Score: {self.score_system.score}"
        level_text = f"Level: {self.level_system.level}"
        
        text_surface = self.font.render(score_text, True, Colors.WHITE.value)
        level_surface = self.font.render(level_text, True, Colors.WHITE.value)
        
        self.screen.blit(text_surface, (20, 20))
        self.screen.blit(level_surface, (20, 60))