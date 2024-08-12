import pygame

# Define the draw_crosshair function
def draw_crosshair(screen, x, y):
    # Draw horizontal line
    pygame.draw.line(screen, (255, 255, 255), (x - 10, y), (x + 10, y))
    # Draw vertical line
    pygame.draw.line(screen, (255, 255, 255), (x, y - 10), (x, y + 10))

# Example usage
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black color
    draw_crosshair(screen, 400, 300)  # Draw a crosshair at the center of the screen
    pygame.display.flip()

pygame.quit()
