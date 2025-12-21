class ShipController:
    def __init__(self, input_handler, ship, screen, ship_speed):
        self.input_handler = input_handler
        self.ship = ship
        self.screen = screen
        self.ship_speed = ship_speed

    def update_ship(self):
        if self.input_handler.moving_right and self.ship.image_rect.right < self.screen.get_rect().right:
            self.ship.image_rect.centerx += self.ship_speed
        if self.input_handler.moving_left and self.ship.image_rect.left > 0:
            self.ship.image_rect.centerx -= self.ship_speed
        if self.input_handler.moving_up and self.ship.image_rect.top > 0:
            self.ship.image_rect.centery -= self.ship_speed
        if self.input_handler.moving_down and self.ship.image_rect.bottom < self.screen.get_rect().bottom:
            self.ship.image_rect.centery += self.ship_speed 