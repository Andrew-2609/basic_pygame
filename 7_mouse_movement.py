import pygame

# Initialize pygame
pygame.init()

# Create the display Surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mouse Movement")

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the display
    display_surface.fill((0, 0, 0))

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()
