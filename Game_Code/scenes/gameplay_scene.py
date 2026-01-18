import pygame
from Game_Code.scenes.pause_scene import PauseScene
from Game_Code.core.scene import Scene
from Game_Code.ship import Ship
from Game_Code.ship_controller import ShipController
from Game_Code.input_handler import InputHandler
from Game_Code.game_configs import GameConfigs, Backgrounds


class GameplayScene(Scene):
    def __init__(self, screen, scene_manager):
        super().__init__(screen)
        self.scene_manager = scene_manager
        
        self.ship = Ship(screen)
        self.input_handler = InputHandler()
        self.ship_controller = ShipController(self.input_handler, self.ship, self.screen, GameConfigs.SHIP_SPEED.value)
        
    def handle_events(self, events):
        self.input_handler.process_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.scene_manager.push(PauseScene(self.screen, self.scene_manager, self))
        
    def update(self):
        self.ship_controller.update_ship()

    def render(self):
        self.screen.blit(Backgrounds().level1_screen, (GameConfigs.SCREEN_WIDTH_BACKGROUND.value, GameConfigs.SCREEN_HEIGHT_BACKGROUND.value))
        self.ship.blitme()