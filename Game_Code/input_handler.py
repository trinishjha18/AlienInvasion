import pygame

class InputHandler:
    def __init__(self):
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.fire = False

    def process_events(self, events):
        self.fire = False
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.key_down(event.key)
            elif event.type == pygame.KEYUP:
                self.key_up(event.key)

    
    def key_down(self, key):
        if key == pygame.K_RIGHT:
            self.moving_right = True
        elif key == pygame.K_LEFT:
            self.moving_left = True
        elif key == pygame.K_UP:
            self.moving_up = True
        elif key == pygame.K_DOWN:
            self.moving_down = True
        elif key == pygame.K_SPACE:
            self.fire = True

    def key_up(self, key):
        if key == pygame.K_RIGHT:
            self.moving_right = False
        elif key == pygame.K_LEFT:
            self.moving_left = False
        elif key == pygame.K_UP:
            self.moving_up = False
        elif key == pygame.K_DOWN:
            self.moving_down = False