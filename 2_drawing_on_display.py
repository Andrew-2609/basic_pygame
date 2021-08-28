import pygame

# Initialize pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

# Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
UCHIHA = (255, 30, 29)

# Give a background color to the display
display_surface.fill(WHITE)

# Draw various shapes on our display
# Line ( surface, color, starting point, ending point, thickness )
# pygame.draw.line(display_surface, WHITE, (0, 0), (100, 100), 5)
# pygame.draw.line(display_surface, WHITE, (100, 100), (599, 300), 5)

# Circle ( surface, color, center, radius, thickness... 0 for fill )
pygame.draw.circle(display_surface, BLACK, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50), 210, 10)
pygame.draw.circle(display_surface, UCHIHA, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50), 200, 0)

# Rectangles ( surface, color, (top-left x, top-left y, width, height) )
pygame.draw.rect(display_surface, BLACK, (240, 450, 120, 360))

pygame.draw.circle(display_surface, BLACK, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 15), 157, 10)
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 15), 147, 0)

pygame.draw.rect(display_surface, WHITE, (250, 450, 100, 350))

# The main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# End the game
pygame.quit()
