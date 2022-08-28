import pygame

from pawn import Pawn
from rook import Rook
from knight import Knight
from king import King
from queen import Queen
from bishop import Bishop

class Grid():

    def __init__(self, size, field_number, color1, color2):
        self.size = size
        self.field_number = field_number
        self.field_size = size / field_number
        self.colors = [color1, color2]

    def show(self, win):
        for i_col, col in enumerate(range(self.field_number)):
            for i_row, row in enumerate(range(self.field_number)):
                # Don't fucking ask this fucking index is fucking magic
                color_index = (i_col * (self.field_number - 1) + i_row) % 2 == 0

                rect = pygame.Rect(self.field_size * row, self.field_size * col, self.field_size, self.field_size)
                
                pygame.draw.rect(win, self.colors[color_index], rect)

    def showChessboard(self, win, chessboard):

        pygame.font.init()

        font = pygame.font.SysFont('Arial', 24)

        figureImages = {Rook : 'R', Knight : 'H', Bishop : 'B', Queen : 'Q', King : 'K', Pawn : 'P'}

        for y, row in enumerate(chessboard):
            for x, figure in enumerate(row):
                if figure != None:
                    color = 'B'
                    if not figure.grp:
                        color = 'W'

                    # img = font.render(figureImages.get(type(figure)), True, color)
                    img = pygame.image.load('assets/images/figures/' + str(figureImages.get(type(figure))) + color + '.png')
                    win.blit(img, (x * self.field_size, y * self.field_size))
