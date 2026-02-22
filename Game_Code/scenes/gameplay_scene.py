import pygame
from Game_Code.scenes.pause_scene import PauseScene
from Game_Code.core.scene import Scene
from Game_Code.ship import Ship
from Game_Code.ship_controller import ShipController
from Game_Code.input_handler import InputHandler
from Game_Code.game_configs import GameConfigs, Backgrounds
from Game_Code.bullets.bullet_manager import BulletManager
from Game_Code.aliens.alien_fleet_manager import AlienFleetManager
from Game_Code.systems.score_system import ScoreSystem
from Game_Code.systems.collision_system import CollisionSystem
from Game_Code.ui.hud import HUD
from Game_Code.systems.level_system import LevelSystem


class GameplayScene(Scene):
    def __init__(self, screen, scene_manager):
        super().__init__(screen)
        self.scene_manager = scene_manager
        
        self.ship = Ship(screen)
        self.input_handler = InputHandler()
        self.ship_controller = ShipController(self.input_handler, self.ship, self.screen, GameConfigs.SHIP_SPEED.value)
        
        self.bullet_manager = BulletManager(screen)
        self.level_system = LevelSystem()
        self.alien_fleet = AlienFleetManager(screen, self.level_system.level)

        self.score_system = ScoreSystem()
        self.collision = CollisionSystem(self.bullet_manager, self.alien_fleet, self.score_system)
        
        self.hud = HUD(screen, self.score_system, self.level_system)

    def handle_events(self, events):
        self.input_handler.process_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.scene_manager.push(PauseScene(self.screen, self.scene_manager, self))
        
        if self.input_handler.fire:
            self.bullet_manager.shoot(self.ship.image_rect)

    def update(self):
        self.ship_controller.update_ship()
        self.bullet_manager.update()
        self.alien_fleet.update()
        self.collision.update()
        
        if not self.alien_fleet.aliens:
            self.level_system.next_level()
            self.ship_controller.increase_speed(1)
            self.alien_fleet = AlienFleetManager(self.screen, self.level_system.level)
            self.collision.set_alien_fleet(self.alien_fleet)
            

    def render(self):
        self.screen.blit(Backgrounds().level1_screen, (GameConfigs.SCREEN_WIDTH_BACKGROUND.value, GameConfigs.SCREEN_HEIGHT_BACKGROUND.value))
        self.bullet_manager.draw()
        self.ship.blitme()
        self.alien_fleet.draw()
        self.hud.draw()