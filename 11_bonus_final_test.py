from random import randrange

import pygame

# Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Final Test")

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5
score = 0

# Load images
dino_image = pygame.image.load("left_dino.png")
dino_image = pygame.transform.flip(dino_image, True, False)
dino_rect = dino_image.get_rect()
dino_rect.topleft = (25, 25)

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Define colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Load fonts
game_font = pygame.font.Font("Mandhor-ALEmp.otf", 32)

# Define texts
main_title = game_font.render("Test of All Content Learned", True, BLACK)
main_title_rect = main_title.get_rect()
main_title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Loading sound effects
sf_coin = pygame.mixer.Sound("sf_sound.wav")
sf_coin.set_volume(.5)

# Load background music
pygame.mixer.music.load("collision_bgm.wav")
pygame.mixer.music.play(-1, 0)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    # Move the dinosaur continuously
    if keys[pygame.K_LEFT] and dino_rect.left > 0:
        dino_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and dino_rect.right < WINDOW_WIDTH:
        dino_rect.x += VELOCITY
    if keys[pygame.K_UP] and dino_rect.top > 0:
        dino_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and dino_rect.bottom < WINDOW_HEIGHT:
        dino_rect.y += VELOCITY

    # Defining a score label
    score_label = game_font.render(f"Score: {score}", True, RED)
    score_label_rect = score_label.get_rect()
    score_label_rect.topright = (WINDOW_WIDTH - 32, 16)

    # Check for collision between two rects
    if dino_rect.colliderect(coin_rect):
        coin_rect.left = randrange(WINDOW_WIDTH - 32)
        coin_rect.top = randrange(WINDOW_HEIGHT - 32)
        score += 1
        sf_coin.play()

    # Fill the display surface
    display_surface.fill((255, 255, 255))

    # Draw rectangles to represent the rect's of each object
    pygame.draw.rect(display_surface, RED, dino_rect, 1)
    pygame.draw.rect(display_surface, YELLOW, coin_rect, 1)

    # Blit (copy) the assets into display
    display_surface.blit(main_title, main_title_rect)
    display_surface.blit(score_label, score_label_rect)
    display_surface.blit(dino_image, dino_rect)
    display_surface.blit(coin_image, coin_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()
