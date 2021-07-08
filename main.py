import pygame
import sys

CLOCK = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (131, 131, 131)
WINDOW_HEIGHT = 800 #Pixel height of grid
WINDOW_WIDTH = 800 #Pixel width of grid
BLOCK_SIZE = 100  #Set the size of the grid block
GRID_WIDTH = int(WINDOW_WIDTH / BLOCK_SIZE) #Cell width of grid
GRID_HEIGHT = int(WINDOW_HEIGHT / BLOCK_SIZE) #Cell height of grid


def drawGrid():
    white = True
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if white:
                pygame.draw.rect(SCREEN, WHITE, rect)
            else:
                pygame.draw.rect(SCREEN, GRAY, rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
            white = not white
        if x % 2 == 0:
            white = False
        else:
            white = True


def main():
    global SCREEN
    pygame.init()
    pygame.display.set_caption("Travis Hescox- Checkers")
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    SCREEN.fill(WHITE)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()