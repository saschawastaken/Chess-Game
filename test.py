from pydoc import render_doc
from shutil import copy2
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

chessboard1 = [
    [Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True), Rook(True)],
    [Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True)],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, Queen(False), None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False)],
    [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False), Rook(False)]
]

chessboard2 = [
    [Rook(True), None, None, Bishop(True), King(True), Bishop(True), Knight(True), Rook(True)],
    [Pawn(True), None, Bishop(True), None, Pawn(True), Pawn(True), Pawn(True), Pawn(True)],
    [None, None, None, None, None, None, None, None],
    [None, Bishop(False), None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False)],
    [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False), Rook(False)]
]


PLAYERS = {0 : 'White', 1 : 'Black'}
TURN = False
GAME_OVER = False

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

    # GET THE POSITION OF THE KING    
    king_grp = not latest_turn
    king_pos = getKingPos(chessboard, king_grp)

    # print(king_pos)

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
                                    saving_chessboard = chessboard_copy
                                    return False
        
        return True

    return False



"""
print(isCheckMate(chessboard1, False))

win.fill((255,255,255))

Grid.show(win)
Grid.showChessboard(win, chessboard1)

pygame.display.update()

input()
"""

print(isCheckMate(chessboard2, False))

win.fill((255,255,255))

Grid.show(win)
Grid.showChessboard(win, chessboard2)

pygame.display.update()

input()

