import sys
import pygame
from src.python import rungame
from src.python import highscores
from src.python import helpscreen
from src.python import shortcuts
from src.python.gameobjects import Text
from src.python.gameobjects import Button


next_task = -1
def start_game():
    global next_task
    next_task = 0
def show_highscores():
    global next_task
    next_task = 1
def load_help():
    global next_task
    next_task = 2
def show_shortcuts():
    global next_task
    next_task = 3

def check_events(start, highscores, help_, shortcut, exit_):
    for event in pygame.event.get():
        start.check_event(event)
        highscores.check_event(event)
        help_.check_event(event)
        shortcut.check_event(event)
        exit_.check_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

def main(screen):
    global next_task
    screen_rect = screen.get_rect()
    welcome = Text(screen, "Welcome...!", 25, position=(screen_rect.centerx, 90))
    start = Button(screen, 190, 25, (0, 0, 0), (screen_rect.centerx, 140), "Start", 20, (255, 255, 255), onclick=start_game, shortcut=pygame.K_s)
    highscore = Button(screen, 190, 25, (0, 0, 0), (screen_rect.centerx, 175), "Highscores", 20, (255, 255, 255), onclick=show_highscores, shortcut=pygame.K_h)
    help_ = Button(screen, 190, 25, (0, 0, 0), (screen_rect.centerx, 210), "Help", 20, (255, 255, 255), onclick=load_help, shortcut=pygame.K_i)
    shortcut = Button(screen, 190, 25, (0, 0, 0), (screen_rect.centerx, 245), "Keyboard Shortcuts[press z]", 20, (255, 255, 255), onclick=show_shortcuts, shortcut=pygame.K_z)
    exit_ = Button(screen, 190, 25, (0, 0, 0), (screen_rect.centerx, 280), "Exit", 20, (255, 255, 255), onclick=sys.exit, shortcut=pygame.K_ESCAPE)
    
    while True:
        check_events(start, highscore, help_, shortcut, exit_)
        if next_task >= 0:
            break
        screen.fill((255, 255, 255))
        welcome.draw()
        start.draw()
        help_.draw()
        highscore.draw()
        shortcut.draw()
        exit_.draw()
        pygame.display.flip()
    
    task_list = [rungame.main, highscores.main, helpscreen.main, shortcuts.main]
    task_list[next_task](screen)
    