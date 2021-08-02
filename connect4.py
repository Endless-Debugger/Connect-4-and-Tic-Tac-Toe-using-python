import numpy
import pygame
import math
import time
ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 245)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (245, 0, 0)
BLACK = (0, 0, 0)
game_over = False
turn = 0
SQUARESIZE = 100
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
RADIUS = int(SQUARESIZE/2 - 5)
SIZE = (WIDTH, HEIGHT)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('monospace', 75)


def create_board():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, col, row, piece):
    board[row][col] = piece


def is_valid_position(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):

    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row


def print_board(board):
    print(numpy.flip(board, 0))


def winning_move(board, piece):
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE/2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

board = create_board()
pygame.init()
screen = pygame.display.set_mode(SIZE)
draw_board(board)
pygame.display.update()
clock.tick(90)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            elif turn == 1:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
            if turn == 0:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARESIZE))
                if is_valid_position(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, col, row, 1)
                    print_board(board)
                    if winning_move(board, piece=1):
                        label = font.render("RED WINS", 1, RED)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        time.sleep(1)
                        game_over = True
                else:
                    label = font.render("It is a tie", 1, WHITE)
                    screen.blit(label, (40, 10))
                    pygame.display.update()
                    time.sleep(1)
                    game_over = True

            elif turn == 1:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / SQUARESIZE))
                if is_valid_position(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, col, row, 2)
                    print_board(board)
                    if winning_move(board, piece=2):
                        label = font.render('YELLOW WINS', 1, YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        time.sleep(1)
                        game_over = True
                else:
                    label = font.render("It is a tie", 1, WHITE)
                    screen.blit(label, (40, 10))
                    pygame.display.update()
                    time.sleep(1)
                    game_over = True
            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2



