from Game_Code.aliens.alien import Alien


class AlienFleetManager:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        
        self.aliens = []

        # If positive value, move to the right, if negative go left
        self.direction = 1
        self.speed = 2 + level # speed scales
        self.drop_distance = 30

        self._create_fleet()

    def _create_fleet(self):
        start_x = 100
        start_y = 60
        spacing_x = 120
        spacing_y = 120

        rows = 3
        columns = 8

        for row in range(rows):
            for column in range(columns):
                x = start_x + (column * spacing_x)
                y = start_y + (row * spacing_y)
                self.aliens.append(Alien(self.screen, x, y, self.level))

    def update(self):
        edge_hit = False

        for alien in self.aliens:
            alien.update(self.speed * self.direction, 0)
            if alien.rect.right >= self.screen.get_rect().right or alien.rect.left <= 0:
                edge_hit = True
        
        if edge_hit:
            self.direction *= -1
            for alien in self.aliens:
                alien.update(0, self.drop_distance)

    def draw(self):
        for alien in self.aliens:
            alien.draw()