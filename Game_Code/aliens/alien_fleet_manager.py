
from Game_Code.aliens.alien import Alien


class AlienFleetManager:
    def __init__(self, screen):
        self.screen = screen
        self.aliens = []
        
        self.direction = 1 # 1 = right, -1 = left
        self.speed = 2
        self.drop_distance = 30
        
        self._create_fleet()
        
    def _create_fleet(self):
        start_x = 100
        start_y = 60
        spacing_x = 80
        spacing_y = 80
        
        rows = 3
        cols = 8
        
        for row in range(rows):
            for col in range(cols):
                x = start_x + (col * spacing_x)
                y = start_y + (row * spacing_y)
                self.aliens.append(Alien(self.screen, x, y))
                
    def update(self):
        edge_hit = False
        
        for alien in self.aliens:
            alien.update(self.speed * self.direction, 0)
            if alien.rect.right >= self.screen.get_rect().right or alien.rect.left <= 0:
                edge_hit = True
                
        if edge_hit == True:
            self.direction *= -1
            for alien in self.aliens:
                alien.update(0, self.drop_distance)
                
    def draw(self):
        for alien in self.aliens:
            alien.draw()