import pygame

# Initialize pygame
pygame.init()

# Create a display Surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds")

# Loading sound effects
sound_1 = pygame.mixer.Sound("sound_1.wav")
sound_2 = pygame.mixer.Sound("sound_2.wav")

# PLay the sound effects
sound_1.play()
pygame.time.delay(int(sound_1.get_length()) * 1000)
sound_2.play()
pygame.time.delay(2000)

# Change the volume of the sound effect
sound_2.set_volume(.1)
sound_2.play()

# Load background music
pygame.mixer.music.load("music.wav")

# Play and stop
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(2000)
sound_1.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

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
