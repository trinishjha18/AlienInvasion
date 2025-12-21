import pygame

class InputHandler:
    def __init__(self):
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                self.key_down(event.key)
            elif event.type == pygame.KEYUP:
                self.key_up(event.key)
        return True
    
    def key_down(self, key):
        if key == pygame.K_RIGHT:
            self.moving_right = True
        if key == pygame.K_LEFT:
            self.moving_left = True
        if key == pygame.K_UP:
            self.moving_up = True
        if key == pygame.K_DOWN:
            self.moving_down = True

    def key_up(self, key):
        if key == pygame.K_RIGHT:
            self.moving_right = False
        if key == pygame.K_LEFT:
            self.moving_left = False
        if key == pygame.K_UP:
            self.moving_up = False
        if key == pygame.K_DOWN:
            self.moving_down = False