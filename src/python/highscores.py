import sys
import datetime
import json
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
    back = Button(screen, 35, 20, (0, 0, 0), (10, 10), "Back", 15, (255, 255, 255), place="left", onclick=go_back)
    t_rank = Text(screen, "Rank", 18, position=(screen_rect.centerx - 135, screen_rect.centery - 150), place="left")
    t_score = Text(screen, "Score", 18, position=(screen_rect.centerx - 45, screen_rect.centery - 150), place="left")
    t_time = Text(screen, "Time", 18, position=(screen_rect.centerx + 60, screen_rect.centery - 150), place="left")
    try:
        with open("src/.highscores.json") as f:
            records = json.load(f)
    except FileNotFoundError:
        records = []
    no_records = ''
    ranks = []
    scores = list()
    times = list()
    if not records:
        no_records = Text(screen, "No record exists.", 20)
    elif not records['scores']:
        no_records = Text(screen, "No record exists.", 20)
    else:
        for sc, time in zip(*records.values()):
            i = len(scores) + 1
            rank = Text(screen, str(i), 18, position=(screen_rect.centerx - 125, (screen_rect.centery - 150) + (i * 25)), place="left")
            ranks.append(rank)
            score = Text(screen, str(sc), 18, position=(screen_rect.centerx - 35, (screen_rect.centery - 150) + (i * 25)), place="left")
            scores.append(score)
            time = datetime.datetime.fromtimestamp(float(time)).strftime("%d-%B-%Y %I:%M %p")
            time = Text(screen, time, 18, position=(screen_rect.centerx + 35, (screen_rect.centery - 150) + (i * 25)), place="left")
            times.append(time)
    
    while True:
        check_events(back)
        if to_return:
            break
        screen.fill((255, 255, 255))
        back.draw()
        if not no_records:
            t_rank.draw()
            t_score.draw()
            t_time.draw()
            for i in range(len(ranks)):
                ranks[i].draw()
                scores[i].draw()
                times[i].draw()
        if no_records:
            no_records.draw() 
        pygame.display.flip()
    
    to_return = False
    homescreen.main(screen)