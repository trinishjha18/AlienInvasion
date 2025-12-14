import pygame
from Game_code.game import AlienInvasion

def main():
    game = AlienInvasion()
    game.run()
    pygame.quit()
    
if __name__ == "__main__":
    main()
