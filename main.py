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

# Game Logic
PLAYERS = {0 : 'White', 1 : 'Black'}
TURN = False
GAME_OVER = False

chessboard = [
    [Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), None, None],
    [Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(False)],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(True)],
    [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), None, None]
]

Grid = Grid(500, 8, (255,255,255), (0,0,0))

# Screen
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load('assets/images/chess_logo.png'))

def copy2dArray(array):
    cp = []
    for row in array:
        cp.append(row.copy())
    return cp

def getKingPos(chessboard, grp):
    for y, row in enumerate(chessboard):
        for x, figure in enumerate(row):
            if type(figure) == King and figure.grp == grp:
                return (y, x)

def isCheck(chessboard, latest_turn):
   
    king_grp = not latest_turn
    king_pos = getKingPos(chessboard, king_grp)

    for y, row in enumerate(chessboard):
        for x, figure in enumerate(row):
            if figure != None and figure.grp == latest_turn:
                if figure.isMoveValid((y, x), king_pos, chessboard):
                    return True

    return False

def isCheckMate(chessboard, latest_turn):

    if isCheck(chessboard, latest_turn):

        king_grp = not latest_turn

        for y, row in enumerate(chessboard):
            for x, figure in enumerate(row):
                if figure != None and figure.grp == king_grp:
                    for target_y in range(8):
                        for target_x in range(8):
                            if figure.isMoveValid((y, x), (target_y, target_x), chessboard):
                                chessboard_copy = copy2dArray(chessboard)

                                chessboard_copy[y][x] = None
                                chessboard_copy[target_y][target_x] = figure

                                if not isCheck(chessboard_copy, latest_turn):
                                    return False
        
        return True

    return False

while not GAME_OVER:

    if isCheckMate(chessboard, not TURN):
        GAME_OVER = True
        break
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Get clicked field positions
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
                
                    chessboard_copy = copy2dArray(chessboard)

                    # Pawn Promotion
                    if type(selectedFigure) == Pawn and selectedFigure.grp and target_y == 7 or type(selectedFigure) == Pawn and not selectedFigure.grp and target_y == 0:
                        chessboard_copy[target_y][target_x] = Queen(selectedFigure.grp)
                    else:
                        chessboard_copy[target_y][target_x] = chessboard_copy[mouse_y][mouse_x]

                    chessboard_copy[mouse_y][mouse_x] = None

                    if not isCheck(chessboard_copy, not TURN): 
                        chessboard = chessboard_copy
                        TURN = not TURN
                    
                else:
                    print('Invalid move')
                
            else:
                print('Invalid figure')

    win.fill((255,255,255))

    Grid.show(win)
    Grid.showChessboard(win, chessboard)

    pygame.display.update()

king_pos = getKingPos(chessboard, not TURN)

text = "Player " + PLAYERS[chessboard[king_pos[0]][king_pos[1]].grp] + " won!"

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