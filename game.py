import pygame
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Set up the display (Width, Height)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 3. Set window title
pygame.display.set_caption("nigga")

# 4. Set up the game clock (controls frame rate)
clock = pygame.time.Clock()

# Main Game Loop
running = True
while running:
    # 5. Event Handling Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Clicking the 'X' button
            running = False

    # 6. Game Logic (Update positions, scores, etc.) goes here

    # 7. Fill the screen background (RGB color)
    screen.fill((40, 44, 52))  # Dark gray color

    # 8. Render game objects here (Shapes, text, images)

    # 9. Update the full display Surface to the screen
    pygame.display.flip()

    # 10. Limit the frame rate to 60 FPS
    clock.tick(60)

# Clean quit when the loop finishes
pygame.quit()
sys.exit()
