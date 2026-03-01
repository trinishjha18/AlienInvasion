import pygame
from Game_Code.core.scene import Scene
from Game_Code.game_configs import Colors


class GameOverScene(Scene):
    def __init__(self, screen, scene_manager, score, level):
        super().__init__(screen)
        self.scene_manager = scene_manager
        self.final_score = score
        self.final_level = level
        self.font = pygame.font.SysFont(None, 64)
        self.small_font = pygame.font.SysFont(None, 36)
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart
                    self.scene_manager.load_scene("menu")
                    
    def update(self):
        pass
    
    def render(self):
        self.screen.fill(Colors.BLACK.value)
        
        title = self.font.render("GAME OVER", True, Colors.WHITE.value)
        title_rect = title.get_rect(center=(self.screen.get_rect().centerx, 200))
        self.screen.blit(title, title_rect)
        
        info = self.small_font.render(
            f"Level: {self.final_level}    Score: {self.final_score}",
            True,
            Colors.WHITE.value
        )
        info_rect = info.get_rect(center=(self.screen.get_rect().centerx, 300))
        self.screen.blit(info, info_rect)
        
        hint = self.small_font.render("Press R to Restart", True, Colors.WHITE.value)
        hint_rect = hint.get_rect(center=(self.screen.get_rect().centerx, 380))
        self.screen.blit(hint, hint_rect)