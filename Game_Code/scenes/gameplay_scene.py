import pygame
from Game_Code.core.scene import Scene
from Game_Code.ship import Ship
from Game_Code.ship_controller import ShipController
from Game_Code.input_handler import InputHandler
from Game_Code.game_configs import Colors, GameConfigs


class GameplayScene(Scene):
    def __init__(self, screen, scene_manager):
        super().__init__(screen)
        self.scene_manager = scene_manager
        
        self.ship = Ship(screen)
        self.input_handler = InputHandler()
        self.ship_controller = ShipController(self.input_handler, self.ship, self.screen, GameConfigs.SHIP_SPEED.value)
        
    def handle_events(self, events):
        self.input_handler.process_events(events)
        
    def update(self):
        self.ship_controller.update_ship()

    def render(self):
        self.screen.fill(Colors.BLACK.value)
        self.ship.blitme()