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
    shortcut_list = {
        "s": "Starts the game [works in Homescreen]",
        "h": "Shows instrustion about game [works in Homescreen]",
        "i": "Shows Highscores [works in Homescreen]",
        "z": "Shows shortcut list [works in Homescreen]",
        "space": "Restarts the game [works after gameover]",
        "backspace": "Return to Homescreen [works anywhere]",
        "escape": "Exits game [works anywhere]"
	}
    messages = list()
    t_key = Text(screen, "Key", 20, position=(screen_rect.centerx - 140, 50))
    t_action = Text(screen, "Action", 20, position=(screen_rect.centerx + 45, 50))
    for key, action in shortcut_list.items():
        i = len(messages) + 1
        key = Text(screen, key, 20, position=(screen_rect.centerx - 140, 50 + (i * 35)))
        action = Text(screen, action, 20, position=(screen_rect.centerx + 45, 50 + (i * 35)))
        messages.append((key, action))
    back = Button(screen, 35, 20, (0, 0, 0), (10, 10), "Back", 15, (255, 255, 255), place="left", onclick=go_back)
    
    while True:
        check_events(back)
        if to_return:
            break
        screen.fill((255, 255, 255))
        t_key.draw()
        t_action.draw()
        for message in messages:
            message[0].draw()
            message[1].draw()
        back.draw()
        pygame.display.flip()
    
    to_return = False
    homescreen.main(screen)