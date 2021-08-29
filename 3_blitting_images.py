import pygame

# Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display_surface.fill((255, 255, 255))
pygame.display.set_caption("Blitting Images")

# Create images... returns a Surface object with the image drawn on it
# We can then get the rect of the Surface and use it to position the image
dino_left_image = pygame.image.load("left_dino.png")
dino_left_rect = dino_left_image.get_rect()
dino_left_rect.topleft = (0, 0)

# THe main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit (copy) a Surface object at the given coordinates to our display
    display_surface.blit(dino_left_image, dino_left_rect)

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()
