import pygame
from Game_code.game_enums import GameSettings
from Game_code.core.scene_manager import SceneManager

class AlienInvasion:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(
            (GameSettings.SCREEN_WIDTH.value, GameSettings.SCREEN_HEIGHT.value)) 
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
            self.clock.tick(GameSettings.FPS.value)
