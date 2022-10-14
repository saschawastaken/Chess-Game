import pygame
from button import Button

def start_menu():

    def getText(text, size, fontStyle, color, isBald=False):
        font = pygame.font.SysFont(fontStyle, size)
        rendered = font.render(text, isBald, color)
        return rendered

    def displayText(win, text, text_rect, fontsize, fontstyle, color, isBald=False):
        rendered_text = getText(text, fontsize, fontstyle, color, isBald)
        win.blit(rendered_text, [text_rect.left + (text_rect[2] - rendered_text.get_width()) / 2, text_rect.top + (text_rect[3] - rendered_text.get_height()) / 2])

    def b_start_func():
        print("Click!")

    b_start = Button("Start", b_start_func, (139,69,19), (205,133,63), (0,0,0), (0,0,0), 20, 'Arial')

    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Chess: Menu")

    pygame.font.init()

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

start_menu()