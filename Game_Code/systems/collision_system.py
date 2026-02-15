class CollisionSystem:
    def __init__(self, bullet_manager, alien_fleet_manager, score_system):
        self.bullet_manager = bullet_manager
        self.alien_fleet_manager = alien_fleet_manager
        self.score_system = score_system
        
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