# import sys
import pygame

def run_game():
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 800))
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption("Alien Invasion")
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill("purple")
        
        pygame.display.flip()
        
        clock.tick(60)
    
    pygame.quit()
     
if __name__ == "__main__":
    run_game()