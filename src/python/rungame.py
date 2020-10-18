import sys
import time
import json
import datetime
import pygame
from src.python import gameover
from src.python.gameobjects import Snack
from src.python.gameobjects import Frog
from src.python.gameobjects import Text
from src.python.gameobjects import Button


gameisover = False
score = prev_score = 0
highscores = []
beaten_highscore = False

def manage_score(score_text, highscore_text):
    global score
    global prev_score
    global beaten_highscore
    if score != prev_score:
        score_text.update_text(f'Score: {score}')
        prev_score = score
    if beaten_highscore or highscores[0] < score:
        highscore_text.update_text(f"Highscore: {score}")
    score_text.draw()
    highscore_text.draw()

def save_record():
    try:
        with open("src/.highscores.json") as f:
            records = json.load(f)
    except FileNotFoundError:
            records = {"scores": [], "timestamps": []}
    record_rank = None
    for i in range(len(records['scores'])):
        if score > records['scores'][i]:
            record_rank = i
            break
    if type(record_rank) is not int:
        if len(records['scores']) < 10 and score != 0:
            record_rank = len(records['scores'])
        else:
            return
    record_timestamp = datetime.datetime.now().timestamp()
    records['scores'].insert(record_rank, score)
    records['timestamps'].insert(record_rank, record_timestamp)
    while len(records['scores']) > 10:
        records['scores'].pop()
        records['timestamps'].pop()
    with open("src/.highscores.json", 'w') as f:
        json.dump(records, f)

def check_collide(snack, frog):
    global gameisover
    temp_rect = pygame.Rect(0, 0, snack.head.width - 3, snack.head.height - 3)
    temp_rect.center = snack.head.center
    if temp_rect.colliderect(frog):
        global score
        frog.reappear()
        snack.grow()
        snack.grow()
        score += 1
    temp_rect = pygame.Rect(0, 0, snack.tail.width - 2, snack.tail.height)
    temp_rect.centery = snack.tail.centery
    temp_rect.left = snack.tail.left
    if snack.head.colliderect(temp_rect):
        gameisover = True
    for i, cell in enumerate(snack.cells.sprites()):
        if cell.direction != snack.head_direction and snack.head.colliderect(cell):
            if i >= 4:
                gameisover = True

def check_events(snack):
    global gameisover
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_UP:
                snack.turn("up")
            if event.key == pygame.K_DOWN:
                snack.turn("down")
            if event.key == pygame.K_LEFT:
                snack.turn("left")
            if event.key == pygame.K_RIGHT:
                snack.turn("right")



def main(screen):
    global highscores
    global gameisover
    gameover.next_task = -1
    snack = Snack(screen)
    snack.grow()
    snack.grow()
    snack.grow()
    snack.grow()
    frog = Frog(snack)
    score_text = Text(screen, 'Score: 0', 22, position=(15, 15), place="left")
    try:
        with open("src/.highscores.json") as f:
            records = json.load(f)
            highscores = records['scores']
    except FileNotFoundError:
        pass
    if not highscores:
        highscores.append(0)
    highscore_text = highscores[0]
    highscore_text = Text(screen, f"Highscore: {highscore_text}", 22, position=(15, 15), place="right")
    
    while True:
        check_events(snack)
        screen.fill((255, 255, 255))
        snack.move()
        snack.check()
        snack.draw()
        frog.draw()
        check_collide(snack, frog)
        manage_score(score_text, highscore_text)
        if gameisover:
            save_record()
            break
        pygame.display.flip()
    
    gameover.main(snack, frog)