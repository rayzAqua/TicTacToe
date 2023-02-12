import time
import pygame as p
import sys
from CONFIG import *
from Button import Button
import Main as g
import PlayWith as plw


def get_font(size):  # Returns Press-Start-2P in the desired size
    return p.font.Font("Image/font.ttf", size)


def onePlayer():
    print("OnePlayer")
    play_as = plw.play_with_menu()
    if play_as == "X":
        g.main(True, False)
    elif play_as == "O":
        g.main(False, True)


def twoPlayer():
    print("TwoPlayer")
    g.main(True, True)


def main_menu():
    # Khoi tao Main_menu
    p.init()
    BG = p.image.load("Image/bgd.jpg")
    p.display.set_caption("TicTacToe")
    SCREEN = p.display.set_mode((WIDTH, HEIGHT))

    # Vi tri de ve chu, button
    x_pos = WIDTH/2
    y_main_menu = 70
    y1_pos = 180
    y2_pos = 330
    y3_pos = 480
    y_credit = 570

    while True:
        # Set BG
        SCREEN.blit(BG, (0, 0))

        # Draw Main Menu text
        MENU_TEXT = get_font(30).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(x_pos, y_main_menu))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Get cursor position
        MENU_MOUSE_POS = p.mouse.get_pos()

        # Draw Button
        PLAY_BUTTON = Button(image=p.transform.scale(p.image.load("Image/Play Rect.png"), (300, 100)),
                             pos=(x_pos, y1_pos), text_input="1 PLAYER", font=get_font(30), base_color="White",
                             hovering_color="Gray")
        OPTIONS_BUTTON = Button(image=p.transform.scale(p.image.load("Image/Play Rect.png"), (300, 100)),
                                pos=(x_pos, y2_pos), text_input="2 PLAYER", font=get_font(30), base_color="White",
                                hovering_color="Gray")
        QUIT_BUTTON = Button(image=p.transform.scale(p.image.load("Image/Quit Rect.png"), (300, 100)),
                             pos=(x_pos, y3_pos), text_input="QUIT", font=get_font(30), base_color="White",
                             hovering_color="Gray")

        # Ve credit
        credits_text = get_font(12).render("Created by group 24", True, "Black")
        credits_rect = credits_text.get_rect(center=(x_pos, y_credit))
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
                    onePlayer()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    time.sleep(0.3)
                    twoPlayer()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    time.sleep(0.3)
                    p.quit()
                    sys.exit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    time.sleep(0.3)
                    p.quit()
                    sys.exit()

        p.display.flip()


if __name__ == "__main__":
    main_menu()