import pygame

# Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Continuous Keyboard Movement")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5

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

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()
    print(keys)

    # Move the dinosaur continuously
    if keys[pygame.K_LEFT] and dino_rect.left > 0:
        dino_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and dino_rect.right < WINDOW_WIDTH:
        dino_rect.x += VELOCITY
    if keys[pygame.K_UP] and dino_rect.top > 0:
        dino_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and dino_rect.bottom < WINDOW_HEIGHT:
        dino_rect.y += VELOCITY

    # Fill the display
    display_surface.fill((255, 255, 255))

    # Blit (copy) the assets into the display surface
    display_surface.blit(dino_image, dino_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()
