import time
import pygame as p
import sys
from CONFIG import *
from Button import Button


def get_font(size):  # Returns Press-Start-2P in the desired size
    return p.font.Font("Image/font.ttf", size)


def play_with_menu():
    p.init()
    WIDTH_MENU = WIDTH
    BG = p.image.load("Image/bgd.jpg")
    p.display.set_caption("TicTacToe")
    SCREEN = p.display.set_mode((WIDTH_MENU, HEIGHT))

    running = True
    while running:
        # Set BG
        SCREEN.blit(BG, (0, 0))

        # Draw Main Menu text
        MENU_TEXT = get_font(30).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH_MENU / 2, 70))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Get cursor position
        MENU_MOUSE_POS = p.mouse.get_pos()

        # Draw Button
        PLAY_BUTTON = Button(image=p.transform.scale(p.image.load("Image/Play Rect.png"), (300, 100)), pos=(WIDTH_MENU / 2, 180),
                             text_input="PLAY AS X", font=get_font(30), base_color="White",
                             hovering_color="Gray")
        OPTIONS_BUTTON = Button(image=p.transform.scale(p.image.load("Image/Play Rect.png"), (300, 100)), pos=(WIDTH_MENU / 2, 330),
                                text_input="PLAY AS 0", font=get_font(30), base_color="White",
                                hovering_color="Gray")
        QUIT_BUTTON = Button(image=p.transform.scale(p.image.load("Image/Quit Rect.png"), (300, 100)), pos=(WIDTH_MENU / 2, 480),
                             text_input="QUIT", font=get_font(30), base_color="White", hovering_color="Gray")

        # Draw credit text
        credits_text = get_font(12).render("Created by group 24", True, "Black")
        credits_rect = credits_text.get_rect(center=(WIDTH_MENU / 2, 570))
        SCREEN.blit(credits_text, credits_rect)

        # Ve lai mau sac cac nut len man hinh
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Bat su kien cac nut
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    time.sleep(0.3)
                    return "X"
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    time.sleep(0.3)
                    return "O"
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    time.sleep(0.3)
                    running = False
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    time.sleep(0.3)
                    running = False

        p.display.flip()

