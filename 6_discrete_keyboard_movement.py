import pygame

# Initialize pygame
pygame.init()

# Create a display Surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display_surface.fill((255, 255, 255))
pygame.display.set_caption("Discrete Keyboard Movement")

# Set game values
VELOCITY = 10

# Load in images
dino_image = pygame.image.load("left_dino.png")
dino_image = pygame.transform.flip(dino_image, True, False)
dino_rect = dino_image.get_rect()
dino_rect.centerx = WINDOW_WIDTH // 2
dino_rect.bottom = WINDOW_HEIGHT

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit (copy) assets to the screen
    display_surface.blit(dino_image, dino_rect)

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()
