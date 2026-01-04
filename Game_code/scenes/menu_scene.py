import pygame
from Game_code.core.scene import Scene
from Game_code.scenes.gameplay_scene import GameplayScene
from Game_code.game_enums import Colors

class MenuScene(Scene):
    def __init__(self, screen, scene_manager):
        super().__init__(screen)
        self.scene_manager = scene_manager
        self.font = pygame.font.SysFont(None, 64)
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.scene_manager.load_scene('gameplay')
                    
    def update(self):
        pass
    
    def render(self):
        self.screen.fill(Colors.BLACK.value)
        text = self.font.render("Press Enter to Start", True, Colors.WHITE.value)
        rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, rect)