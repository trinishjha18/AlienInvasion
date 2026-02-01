import pygame
from Game_Code.game_configs import GameConfigs
from Game_Code.core.scene_manager import SceneManager
from Game_Code.scenes.menu_scene import MenuScene


class AlienInvasion:
    def __init__(self):
        # pygame setup
        pygame.init()

        self.screen = pygame.display.set_mode((GameConfigs.SCREEN_WIDTH.value, GameConfigs.SCREEN_HEIGHT.value))
        self.clock = pygame.time.Clock()
        
        self.running = True

        self.scene_manager = SceneManager(self.screen)
        self.scene_manager.load_scene("menu")

       
    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                 if event.type == pygame.QUIT:
                      self.running = False
            
            self.scene_manager.handle_events(events)
            self.scene_manager.update()
            self.scene_manager.render()

            pygame.display.flip()
            self.clock.tick(GameConfigs.FPS.value)
