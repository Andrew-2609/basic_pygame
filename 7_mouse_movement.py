import pygame

# Initialize pygame
pygame.init()

# Create the display Surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display_surface.fill((255, 255, 255))
pygame.display.set_caption("Mouse Movement")

# Load images
dino_image = pygame.image.load("left_dino.png")
dino_image = pygame.transform.flip(dino_image, True, False)
dino_rect = dino_image.get_rect()
dino_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move based on clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dino_rect.center = (mouse_x, mouse_y)

        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            dino_rect.center = (event.pos[0], event.pos[1])

    # Clear the display
    display_surface.fill((255, 255, 255))

    # Blit (copy) the assets to the display surface
    display_surface.blit(dino_image, dino_rect)

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()
