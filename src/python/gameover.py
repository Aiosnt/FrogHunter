import sys
import pygame
from src.python import homescreen
from src.python import rungame
from src.python.gameobjects import Text
from src.python.gameobjects import Button


next_task = -1
def restart_game():
    global next_task
    next_task = 0

def go_back():
    global next_task
    next_task = 1

def check_events(restart, back):
    for event in pygame.event.get():
        back.check_event(event)
        restart.check_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_BACKSPACE:
                go_back()

def main(snack, frog):
    homescreen.next_task = -1
    rungame.gameisover = False
    rungame.score = prev_score = 0
    rungame.highscores = []
    rungame.beaten_highscore = False
    screen_rect = snack.screen.get_rect()
    end_msg = Text(snack.screen, "Game Over!!", 25, position=(screen_rect.centerx, 115))
    restart = Button(snack.screen, 90, 40, (0, 0, 0), (screen_rect.centerx, screen_rect.centery - 35), "Restart", 20, (255, 255, 255), onclick=restart_game, shortcut=pygame.K_SPACE)
    back = Button(snack.screen, 150, 40, (0, 0, 0), (screen_rect.centerx, screen_rect.centery + 25), "Back to Home", 20, (255, 255, 255), onclick=go_back)
    
    while True:
        check_events(restart, back)
        if next_task >= 0:
            break
        snack.screen.fill((255, 255, 255))
        snack.draw()
        frog.draw()
        end_msg.draw()
        restart.draw()
        back.draw()
        pygame.display.flip()
    
    tasks_list = [rungame.main, homescreen.main]
    tasks_list[next_task](snack.screen)