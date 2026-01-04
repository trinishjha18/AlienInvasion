import pygame
from Game_code.scenes.pause_scene import PauseScene
from Game_code.core.scene import Scene
from Game_code.ship import Ship
from Game_code.ship_controller import ShipController
from Game_code.input_handler import InputHandler
from Game_code.game_enums import Colors, GameSettings

class GameplayScene(Scene):
    def __init__(self, screen, scene_manager):
        super().__init__(screen)
        self.scene_manager = scene_manager
        
        self.ship = Ship(screen)
        self.input_handler = InputHandler()
        self.ship_controller = ShipController(self.input_handler, self.screen, self.ship, GameSettings.SHIP_SPEED.value)
        
    def handle_events(self, events):
        self.input_handler.process_events(events)
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.scene_manager.push(
                        PauseScene(self.screen, self.scene_manager, self)
                    )
        
    def update(self):
        self.ship_controller.update_ship()
        
    def render(self):
        self.screen.fill(Colors.BLACK.value)
        self.ship.blitme()