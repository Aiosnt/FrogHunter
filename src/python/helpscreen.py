import sys
import pygame
from src.python import homescreen
from src.python.gameobjects import Text
from src.python.gameobjects import Button


to_return = False
def go_back():
    global to_return
    to_return = True

def check_events(back):
    for event in pygame.event.get():
        back.check_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_BACKSPACE:
                go_back()

def main(screen):
    global to_return
    homescreen.next_task = -1
    screen_rect = screen.get_rect()
    messages = [">>Be the controller of the Snack and chase the Frog!",
        ">>Use the 4 arrow keys to move the snack.",
        ">>Be gentle with keyboard.In order to maintain game performance,",
        "minimum interval between two turn should be 125 miliseconds.",
        "Otherwise the last turn won't effect the game.",
        ">>Press Escape to exit game anywhere"]
    messages[0] = Text(screen, messages[0], 20, position=(screen_rect.centerx, 100))
    messages[1] = Text(screen, messages[1], 20, position=(screen_rect.centerx, 130))
    messages[2] = Text(screen, messages[2], 20, position=(screen_rect.centerx, 160))
    messages[3] = Text(screen, messages[3], 20, position=(screen_rect.centerx, 180))
    messages[4] = Text(screen, messages[4], 20, position=(screen_rect.centerx, 200))
    messages[5] = Text(screen, messages[5], 20, position=(screen_rect.centerx, 230))
    back = Button(screen, 35, 20, (0, 0, 0), (10, 10), "Back", 15, (255, 255, 255), place="left", onclick=go_back)
    
    while True:
        check_events(back)
        if to_return:
            break
        screen.fill((255, 255, 255))
        messages[0].draw()
        messages[1].draw()
        messages[2].draw()
        messages[3].draw()
        messages[4].draw()
        messages[5].draw()
        back.draw()
        pygame.display.flip()
    
    to_return = False
    homescreen.main(screen)