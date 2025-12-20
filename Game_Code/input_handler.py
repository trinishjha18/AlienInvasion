import pygame

class InputHandler:
    def __init__(self):
        # Make sure ship is not continuosly moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the user closes the window running is off
                return False
            elif event.type == pygame.KEYDOWN:
                self.key_down(event.key)
            elif event.type == pygame.KEYUP:
                self.key_up(event.key)
        return True
    
    def key_down(self, key):
        # If right key is pressed move to the right
        if key == pygame.K_RIGHT:
            self.moving_right = True
        # If left key is pressed move to the left
        if key == pygame.K_LEFT:
            self.moving_left = True
        # If up key is pressed move to the up
        if key == pygame.K_UP:
            self.moving_up = True
        # If down key is pressed move to the down
        if key == pygame.K_DOWN:
            self.moving_down = True

    def key_up(self, key):
        # If the right key is not pressed don't move right
        if key == pygame.K_RIGHT:
            self.moving_right = False
        # If the left key is not pressed don't move left
        if key == pygame.K_LEFT:
            self.moving_left = False
        # If the up key is not pressed don't move up
        if key == pygame.K_UP:
            self.moving_up = False
        # If the down key is not pressed don't move down
        if key == pygame.K_DOWN:
            self.moving_down = False