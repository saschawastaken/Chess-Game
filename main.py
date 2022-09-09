from pydoc import render_doc
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
import time

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load('assets/images/chess_logo.png'))

Grid = Grid(500, 8, (255,255,255), (0,0,0))

def copy2dArray(array):
    cp = []
    for row in array:
        cp.append(row.copy())
    return cp

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
                        return (True, king_2_pos)
                else:
                    if figure.isMoveValid((y, x), king_1_pos, chessboard):
                        return (True, king_1_pos)
    
    return (False, None)

def isCheckMate(chessboard, checked_king_pos):

    checkedKing = chessboard[checked_king_pos[0]][checked_king_pos[1]]        

    for y, row in enumerate(chessboard):
        for x, figure in enumerate(row):
            if figure != None and figure.grp == checkedKing.grp:
                
                for pos_y in range(8):
                    for pos_x in range(8):
                        if figure.isMoveValid((y, x), (pos_y, pos_x), chessboard):
                            
                            chessboard_copy = copy2dArray(chessboard)

                            chessboard_copy[pos_y][pos_x] = chessboard_copy[y][x]
                            chessboard_copy[y][x] = None

                            if not isCheck(chessboard_copy):
                                return False
    
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

PLAYERS = {0 : 'White', 1 : 'Black'}
TURN = True
GAME_OVER = False

while not GAME_OVER:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # get clicked field positions
            mouse_x = math.floor(mouse_pos[0] / Grid.field_size)
            mouse_y = math.floor(mouse_pos[1] / Grid.field_size)

            selectedFigure = chessboard[mouse_y][mouse_x]
            
            if selectedFigure != None and selectedFigure.grp == TURN:
                
                print("Select target postition")
                target_x = -1
                target_y = -1

                while target_x < 0 and target_y < 0:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            target_pos = pygame.mouse.get_pos()
                            target_x = math.floor(target_pos[0] / Grid.field_size)
                            target_y = math.floor(target_pos[1] / Grid.field_size)

                if (mouse_y, mouse_x) != (target_y, target_x) and selectedFigure.isMoveValid((mouse_y, mouse_x), (target_y, target_x), chessboard):
                
                    chessboard_copy = chessboard.copy()

                    chessboard_copy[target_y][target_x] = chessboard_copy[mouse_y][mouse_x]
                    chessboard_copy[mouse_y][mouse_x] = None

                    # Check
                    func_check = isCheck(chessboard)
                    checked = func_check[0]

                    if not checked: 
                        chessboard = chessboard_copy

                    else:
                        checked_king_pos = func_check[1]
                        if isCheckMate(chessboard, checked_king_pos):
                            GAME_OVER = True
                            break

                    TURN = not TURN
                else:
                    print('INVALID MOVE')
                
            else:
                print('INVALID FIGURE')

    win.fill((255,255,255))

    Grid.show(win)
    Grid.showChessboard(win, chessboard)

    pygame.display.update()

text = 'Player ' + PLAYERS[not chessboard[checked_king_pos[0]][checked_king_pos[1]].grp] + ' won!'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
                
    win.fill((255,255,255))
    Grid.show(win)
    Grid.showChessboard(win, chessboard)
    
    font = pygame.font.SysFont('Arial', 60)
    rendered_text = font.render(text, True, (255,0,0))

    rendered_text_rect = rendered_text.get_rect()

    win.blit(rendered_text, pygame.Rect(win.get_width() / 2 - rendered_text_rect.width / 2, win.get_height() / 2 - rendered_text_rect.height / 2, rendered_text_rect.width, rendered_text_rect.height))

    pygame.display.update()