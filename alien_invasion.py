import pygame

SCREEN_WIDTH = 1280

IMAGE_WIDTH = 100


# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Load image on the screen
    image = pygame.image.load("Images/Spaceship5.png")
    
    # Resize any image
    image = pygame.transform.scale(image, (IMAGE_WIDTH, 100))
    
    # Get coordinates of image
    image_rect = image.get_rect()
    screen_rect = screen.get_rect()
    
    # Align image and screen together
    image_rect.bottom = screen_rect.bottom
    image_rect.centerx = screen_rect.centerx

    screen.blit(image, image_rect)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()