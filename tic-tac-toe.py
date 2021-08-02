import numpy
import pygame
import time
SQUARESIZE = 200
HALF_SQUARESIZE = 100
ROW_COUNT = 3
COLUMN_COUNT = 3
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = int(ROW_COUNT * SQUARESIZE + SQUARESIZE/2)
SIZE = (WIDTH, HEIGHT)
RADIUS = HALF_SQUARESIZE - 5
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('monospace', 200)
font2 = pygame.font.SysFont('monospace', 75)
screen = pygame.display.set_mode(SIZE)



def create_board():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def is_valid_coordinate(board, row, column):
    if board[row][column] == 0:
        return True
    else:
        print("This place has already been filled!")
        return False


def drop_piece(board, row, column, piece):

    board[row][column] = piece


def is_winner(board, piece):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):

            if board[0][c] == piece and board[1][c] == piece and board[2][c] == piece:
                return True
            if board[0][0] == piece and board[1][1] == piece and board [2][2] == piece:
                return True
            if board[0][2] == piece and board[1][1] == piece and board[2][0] == piece:
                return True
            if board[r][0] == piece and board[r][1] == piece and board[r][2] == piece:
                return True


def draw_board(board, screen):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            pygame.draw.rect(screen, (0, 0, 50), (c * SQUARESIZE, int(r * SQUARESIZE + HALF_SQUARESIZE), SQUARESIZE, SQUARESIZE))
            pygame.draw.rect(screen, (255, 255, 255), (c * SQUARESIZE + 10, int(r * SQUARESIZE + HALF_SQUARESIZE + 10), SQUARESIZE - 20, SQUARESIZE - 20))
            if board[r][c] == 1:
                pygame.draw.circle(screen, (255, 255, 0), (c * SQUARESIZE + HALF_SQUARESIZE, int(r * SQUARESIZE + HALF_SQUARESIZE + HALF_SQUARESIZE)), RADIUS)
            if board[r][c] == 2:
                lable = font.render("X", 1, (255, 0, 0))
                screen.blit(lable, (c * SQUARESIZE + 30, int(r * SQUARESIZE + HALF_SQUARESIZE ), SQUARESIZE - 20, SQUARESIZE - 20))
    pygame.display.update()


board = create_board()

game_over = False
turn = 0

while not game_over:
    draw_board(board, screen)
    column = 10
    row = 10
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 1:
                if 0 <= event.pos[0] <= 200:
                    column = 0
                if 200 <= event.pos[0] <= 400:
                    column = 1
                if 400 <= event.pos[0] <= 600:
                    column = 2
                if 100 <= event.pos[1] <= 300:
                    row = 0
                if 300 <= event.pos[1] <= 500:
                    row = 1
                if 500 <= event.pos[1] <= 700:
                    row = 2

                if is_valid_coordinate(board, row, column):
                    drop_piece(board, row, column, 1)
                if is_winner(board, 1):
                    LABEL = font2.render('Circle Wins', 1, (255, 255, 0))
                    screen.blit(LABEL, (25, 25))
                    draw_board(board, screen)
                    pygame.display.update()

                    time.sleep(1)
                    game_over = True

            elif turn == 0:
                if 0 <= event.pos[0] <= 200:
                    column = 0
                if 200 <= event.pos[0] <= 400:
                    column = 1
                if 400 <= event.pos[0] <= 600:
                    column = 2

                if 100 <= event.pos[1] <= 300:
                    row = 0
                if 300 <= event.pos[1] <= 500:
                    row = 1
                if 500 <= event.pos[1] <= 700:
                    row = 2
                if is_valid_coordinate(board, row, column):
                    drop_piece(board, row, column, 2)
                else:
                    game_over = True
                if is_winner(board, 2):
                    LABEL = font2.render('Cross Wins', 1, (255, 0, 0))
                    screen.blit(LABEL, (25, 25))
                    draw_board(board, screen)
                    pygame.display.update()
                    time.sleep(1)
                    game_over = True

            turn += 1
            turn = turn % 2
            print(board)



