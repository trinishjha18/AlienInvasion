import pygame
from Game_Code.game_configs import Colors
from Game_Code.core.scene import Scene


class PauseScene(Scene):
    def __init__(self, screen, screen_manager, gameplay_scene):
        super().__init__(screen)
        self.scene_manager = screen_manager
        self.gameplay_scene = gameplay_scene

        self.font = pygame.font.SysFont(None, 64)
        self.small_font = pygame.font.SysFont(None, 36)

    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.scene_manager.pop()
                
                elif event.key == pygame.K_ESCAPE:
                    self.scene_manager.load_scene("menu")
    
    def update(self):
        pass

    def render(self):
        self.gameplay_scene.render()

        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        pause_text = self.font.render("PAUSED", True, Colors.WHITE.value)
        resume_text = self.small_font.render("Press P to resume || ESC for Menu", True, Colors.WHITE.value)

        pause_rect = pause_text.get_rect(center=(640, 300))
        resume_rect = resume_text.get_rect(center=(640, 380))

        self.screen.blit(pause_text, pause_rect)
        self.screen.blit(resume_text, resume_rect)
