import pygame

# Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection")

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5

# Load images
dino_image = pygame.image.load("left_dino.png")
dino_image = pygame.transform.flip(dino_image, True, False)
dino_rect = dino_image.get_rect()
dino_rect.topleft = (25, 25)

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the display surface
    display_surface.fill((255, 255, 255))

    # Blit (copy) the assets into display
    display_surface.blit(dino_image, dino_rect)
    display_surface.blit(coin_image, coin_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()
