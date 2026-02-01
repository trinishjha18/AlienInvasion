from Game_Code.bullets.bullets import Bullet


class BulletManager:
    def __init__(self, screen):
        self.screen = screen
        self.bullets = []

    def shoot(self, ship_rect):
        bullet = Bullet(self.screen, ship_rect)
        self.bullets.append(bullet)

    def update(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()