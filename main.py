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
BOARD_POS = (0, 0)
SINGLE_RED = pygame.image.load(r"./graphics/red-piece.png")
KING_RED = pygame.image.load(r"./graphics/red-king.png")
SINGLE_BLACK = pygame.image.load(r"./graphics/black-piece.png")
KING_BLACK = pygame.image.load(r"./graphics/black-king.png")

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


#2d array for storing board state
def setBoard():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)
    for black in range(0, 7, 2):
        board[0][black] = ("black", "single")
    for black in range(1, 8, 2):
        board[1][black] = ("black", "single")
    for black in range(0, 7, 2):
        board[2][black] = ("black", "single")
    for red in range(1, 8, 2):
        board[7][red] = ("red", "single")
    for red in range(0, 7, 2):
        board[6][red] = ("red", "single")
    for red in range(1, 8, 2):
        board[5][red] = ("red", "single")
    return board


#returns the space where the pointer is located
def getSpace(board):
    #gets x, y coordinates of mouse position and
    pointer = pygame.Vector2(pygame.mouse.get_pos()) - BOARD_POS
    #use integer division to get board square
    x, y = [int(coord // BLOCK_SIZE) for coord in pointer]
    try:
        if x >= 0 and y >= 0:
            # returns the boord square and x, y coordinates of pointer location
            return (board[y][x], x, y)
    except IndexError:
        pass
    return None, None, None


#places pieces on the board
def placePieces(SCREEN, board):
    for y in range(8):
        for x in range(8):
            currPiece = board[y][x]
            if currPiece:
                color, type = currPiece
                s1 = SINGLE_RED
                s2 = SINGLE_RED
                pos = pygame.Rect(BOARD_POS[0] + x * BLOCK_SIZE + 1, BOARD_POS[1] + y * BLOCK_SIZE + 1, BLOCK_SIZE, BLOCK_SIZE)
                SCREEN.blit(s2, s2.get_rect(center=pos.center).move(1, 1))
                SCREEN.blit(s1, s1.get_rect(center=pos.center))


def main():
    global SCREEN
    pygame.init()
    pygame.display.set_caption("Travis Hescox- Checkers")
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    SCREEN.fill(WHITE)
    board = setBoard()

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        piece, x, y = getSpace(board)

        if x != None:
            rect = (BOARD_POS[0] + x * BLOCK_SIZE, BOARD_POS[1] + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (255, 0, 0, 50), rect, 2)
        placePieces(SCREEN, board)
        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    main()