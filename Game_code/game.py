import pygame
from Game_code.game_enums import Colors, GameSettings
from Game_code.ship import Ship
from Game_code.input_handler import InputHandler
from Game_code.ship_controller import ShipController

from Game_code.core.scene_manager import SceneManager
from Game_code.scenes.menu_scene import MenuScene



class AlienInvasion:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(
            (GameSettings.SCREEN_WIDTH.value, GameSettings.SCREEN_HEIGHT.value))
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # self.ship = Ship(self.screen)
        # self.ship_speed = GameSettings.SHIP_SPEED.value
        
        # self.input_handler = InputHandler()
        # self.ship_controller = ShipController(self.input_handler, self.screen, self.ship, self.ship_speed)
        
        self.scene_manager = SceneManager(
            MenuScene(self.screen, None)
        )
        
        self.scene_manager.current_scene.scene_manager = self.scene_manager
        
        
    def run(self):
        while self.running:
            # self.running = self.input_handler.process_events()
            # self.ship_controller.update_ship()
            # self.render()
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.scene_manager.handle_events(events)
            self.scene_manager.update()
            self.scene_manager.render()
            
            pygame.display.flip()
            self.clock.tick(GameSettings.FPS.value)
    
    # def render(self):
    #     # Set screen to black
    #     self.screen.fill(Colors.BLACK.value)
    #     # Display image on the screen
    #     self.ship.blitme()
    #     # flip() the display to put your work on screen
    #     pygame.display.flip()