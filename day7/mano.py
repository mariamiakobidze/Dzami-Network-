import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
RED = (204, 51, 255)
BLACK = (0, 102, 255)
SQUARE_SIZE = 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maro Pygame Game")


square_x, square_y = WIDTH // 2 - SQUARE_SIZE // 2, HEIGHT // 2 - SQUARE_SIZE // 2

def draw_square(surface, color, x, y):
    pygame.draw.rect(surface, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

def main():
    global square_x, square_y 
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            square_x -= 5
        if keys[pygame.K_RIGHT]:
            square_x += 5
        if keys[pygame.K_UP]:
            square_y -= 5
        if keys[pygame.K_DOWN]:
            square_y += 5

        screen.fill(BLACK)

        draw_square(screen, RED, square_x, square_y)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()