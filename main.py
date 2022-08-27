from pawn import Pawn
from rook import Rook
from knight import Knight
from king import King
from queen import Queen
from bishop import Bishop
import pygame
from pygame.locals import *
from grid import Grid
import math

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load('assets/images/chess_logo.jpg'))

Grid = Grid(500, 8, (255,255,255), (0,0,0))

def isCheck(chessboard):

    # Get the positions of kings
    king_1_pos = (0, 0)
    king_2_pos = (0, 0)

    for y, row in enumerate(chessboard):
        for x, figure in enumerate(row):
            if type(figure) == King:
                if figure.grp:
                    king_1_pos = (y, x)
                else:
                    king_2_pos = (y, x)

    # Now check if an enemy figure can move on king
    for y, row in enumerate(chessboard):
        for x, figure in enumerate(row):
            if figure != None:
                if type(figure) == Queen and figure.grp == False:
                    """
                    print(figure.isMoveValid((y, x), king_1_pos, chessboard))
                    print(figure.grp)
                    """
                if figure.grp:
                    if figure.isMoveValid((y, x), king_2_pos, chessboard):
                        return True
                else:
                    if figure.isMoveValid((y, x), king_1_pos, chessboard):
                        return True

chessboard = [
    [Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True), Rook(True)],
    [Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True)],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False)],
    [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False), Rook(False)]
]


turn = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # get clicked field positions
            mouse_x = math.floor(mouse_pos[0] / Grid.field_size)
            mouse_y = math.floor(mouse_pos[1] / Grid.field_size)

            selectedFigure = chessboard[mouse_y][mouse_x]
            
            if selectedFigure != None and selectedFigure.grp == turn:

                print("Select target postition")
                target_x = -1
                target_y = -1

                while target_x < 0 and target_y < 0:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            target_pos = pygame.mouse.get_pos()
                            target_x = math.floor(target_pos[0] / Grid.field_size)
                            target_y = math.floor(target_pos[1] / Grid.field_size)

                if selectedFigure.isMoveValid((mouse_y, mouse_x), (target_y, target_x), chessboard):
                
                    chessboard_copy = chessboard.copy()

                    chessboard_copy[target_y][target_x] = chessboard_copy[mouse_y][mouse_x]
                    chessboard_copy[mouse_y][mouse_x] = None

                    if True:
                        
                        chessboard = chessboard_copy

                        turn = not turn
                    else:
                        print('CHECK')
                else:
                    print('INVALID MOVE')

            else:
                print('INVALID FIGURE')

    win.fill((255,255,255))

    Grid.show(win)
    Grid.showChessboard(win, chessboard)

    pygame.display.update()
