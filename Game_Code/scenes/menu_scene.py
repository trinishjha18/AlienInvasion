import pygame
from Game_Code.game_configs import GameConfigs, Backgrounds, Colors
from Game_Code.scenes.gameplay_scene import GameplayScene
from Game_Code.core.scene import Scene
from Game_Code.ship import Ship


class MenuScene(Scene):
    def __init__(self, screen, scene_manager):
        super().__init__(screen)
        self.scene_manager = scene_manager
        self.font = pygame.font.SysFont(None, 64)
        self.ship = Ship(screen)


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.scene_manager.replace(GameplayScene(self.screen, self.scene_manager))
    
    def update(self):
        pass

    def render(self):
        self.screen.blit(Backgrounds().menu_screen, (GameConfigs.SCREEN_WIDTH_BACKGROUND.value, GameConfigs.SCREEN_HEIGHT_BACKGROUND.value))
        text = self.font.render("Press Enter to Start", True, Colors.WHITE.value)
        rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, rect)