from Game_Code.bullets.bullet_manager import BulletManager


class CollisionSystem:
    def __init__(self, bullet_manager, alien_fleet_manager, score_system, ship):
        self.bullet_manager: BulletManager = bullet_manager
        self.alien_fleet_manager = alien_fleet_manager
        self.score_system = score_system
        self.ship = ship

    def set_alien_fleet(self, alien_fleet_manager):
        self.alien_fleet_manager = alien_fleet_manager

    def update(self):
        bullets = self.bullet_manager.bullets
        aliens = self.alien_fleet_manager.aliens

        for bullet in bullets:
            for alien in aliens:
                if bullet.rect.colliderect(alien.rect):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    self.score_system.add_points(10)
                    break
        
        # Alien & Ship Collision System
        ship_rect = self.ship.image_rect
        for alien in aliens:
            if alien.rect.colliderect(ship_rect) or alien.rect.bottom >= ship_rect.top:
                return True
        return False
