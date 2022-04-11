import pygame

screen = pygame.display.set_mode([800, 500])
# Run until the user asks to quit
clock = pygame.time.Clock()
running = True

rect: pygame.Rect = pygame.Rect(20, 20, 50, 50)

# Fill background
screen.fill((120, 200, 255))
 
    # Draw rect (window, color(rgb), rect object)
pygame.draw.rect(screen, (150, 10, 245), rect)