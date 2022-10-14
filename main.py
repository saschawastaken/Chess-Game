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
from button import Button
import math

Grid = Grid(500, 8, (255,255,255), (0,0,0))

def start_menu():

    class ButtonStart(Exception): pass

    def getText(text, size, fontStyle, color, isBald=False):
        font = pygame.font.SysFont(fontStyle, size)
        rendered = font.render(text, isBald, color)
        return rendered

    def displayText(win, text, text_rect, fontsize, fontstyle, color, isBald=False):
        rendered_text = getText(text, fontsize, fontstyle, color, isBald)
        win.blit(rendered_text, [text_rect.left + (text_rect[2] - rendered_text.get_width()) / 2, text_rect.top + (text_rect[3] - rendered_text.get_height()) / 2])

    def b_start_func():
        raise ButtonStart

    b_start = Button("Start", b_start_func, (139,69,19), (205,133,63), (0,0,0), (0,0,0), 20, 'Arial')

    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Chess: Menu")

    pygame.font.init()

    try:
        while True:
            
            mouse_down = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down = True

            win.fill((0,0,0))

            displayText(win, "Chess", pygame.Rect(win.get_width() / 2 - 100 / 2 , 125, 100, 50), 50, 'Arial', (234, 221, 202), True)
            
            b_start.show(win, pygame.Rect(win.get_width() / 2 - 100 / 2 , 275, 100, 50), pygame.mouse.get_pos(), mouse_down)

            pygame.display.update()

    except ButtonStart:
        start_game()

def start_game():

    # Game Logic
    PLAYERS = {0 : 'White', 1 : 'Black'}
    TURN = False
    GAME_OVER = False

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

    # Screen
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Chess: Game')
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
                        pass #print('Invalid move')
                    
                else:
                    pass #print('Invalid figure')

        win.fill((255,255,255))

        Grid.show(win)
        Grid.showChessboard(win, chessboard)

        pygame.display.update()

    king_pos = getKingPos(chessboard, not TURN)

    text = "Player " + PLAYERS[chessboard[king_pos[0]][king_pos[1]].grp] + " won!"

    class ButtonExit(Exception): pass

    def b_exit_func():
        raise ButtonExit

    b_exit = Button("Exit", b_exit_func, (125,0,0), (200,0,0), (0,0,0), (0,0,0), 30, 'Arial')

    try:
        while True:

            mouse_down = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down = True
                        
            win.fill((255,255,255))
            Grid.show(win)
            Grid.showChessboard(win, chessboard)
            
            font = pygame.font.SysFont('Arial', 60)
            rendered_text = font.render(text, True, (255,0,0))

            rendered_text_rect = rendered_text.get_rect()

            win.blit(rendered_text, pygame.Rect(win.get_width() / 2 - rendered_text_rect.width / 2, win.get_height() / 2 - rendered_text_rect.height / 2, rendered_text_rect.width, rendered_text_rect.height))

            b_exit.show(win, pygame.Rect(win.get_width() / 2 - 100 / 2, 325, 100, 50), pygame.mouse.get_pos(), mouse_down)

            pygame.display.update()

    except ButtonExit:
        start_menu()

start_menu()
