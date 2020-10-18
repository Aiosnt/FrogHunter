import random
import time
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Cell(Sprite):
    
    def __init__(self, body):
        super().__init__()
        self.body = body
        self.rect = pygame.Rect(0, 0, 9, 9)
        self.previous = self.body.last_cell
        self.turning_point = tuple()
        if type(self.body.last_cell) is Cell:
            self.rect.center = self.body.last_cell.rect.center
            left, top, right, bottom = self.body.last_cell.rect.left, self.body.last_cell.rect.top, self.body.last_cell.rect.right, self.body.last_cell.rect.bottom
            self.direction = self.body.last_cell.direction
        else:
            self.rect.center = self.body.last_cell.center
            left, top, right, bottom = self.body.last_cell.left, self.body.last_cell.top, self.body.last_cell.right, self.body.last_cell.bottom
            self.direction = self.body.head_direction
        if self.direction == 'left':
            self.rect.left = right
        elif self.direction == 'right':
            self.rect.right = left
        elif self.direction == 'up':
            self.rect.top = bottom
        elif self.direction == 'down':
            self.rect.bottom = top
        try:
            if body.last_cell.color == (16, 115, 45):
                self.color = (0, 75, 0)
                
            else:
                self.color = (16, 115, 45)
        except AttributeError:
            self.color = (16, 115, 45)
        self.turned = 0
    
    def move(self):
        if type(self.previous) is Cell:
            prev_dir = self.previous.direction
            turning_point = self.previous.turning_point
        else:
            prev_dir = self.body.head_direction
            turning_point = self.body.turning_point
        if prev_dir != self.direction:
            if self.rect.center == turning_point:
                self.direction = prev_dir
                self.turning_point = turning_point
        if self.direction == 'left':
            self.rect.x -= 1
        elif self.direction == 'right':
            self.rect.x += 1
        elif self.direction == 'up':
            self.rect.y -= 1
        elif self.direction == 'down':
            self.rect.y += 1
        if self.direction == 'left' and self.rect.left < 0:
            self.rect.left = self.body.screen_rect.right
        elif self.direction == 'right' and self.rect.left > self.body.screen_rect.right:
            self.rect.left = 0
        elif self.direction == 'up' and self.rect.top < 0:
            self.rect.top = self.body.screen_rect.bottom
        elif self.direction == 'down' and self.rect.top > self.body.screen_rect.bottom:
            self.rect.top = 0
    
    def draw(self):
        pygame.draw.rect(self.body.screen, self.color, self.rect)

class Snack:
    
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.cells = Group()
        self.cell_count = 0
        self.head_img = pygame.image.load("src/images/head.bmp")
        self.head = self.head_img.get_rect()
        self.head.centerx = int(self.screen_rect.centerx * 1.5)
        self.head.centery = int(self.screen_rect.centery * 1.5)
        self.last_cell = self.head
        self.tail_img = pygame.image.load("src/images/tail.bmp")
        self.tail = self.tail_img.get_rect()
        self.tail.center = self.last_cell.center
        self.tail.left = self.last_cell.right
        self.head_direction = self.tail_direction = "left"
        self.speed = 1
        self.turning_point = tuple()
        self.last_turn = 0
    
    def turn_head(self, direction):
        if direction == "up":
            if self.head_direction == 'left':
                angle = -90
            elif self.head_direction == 'right':
                angle = 90
            else:
                angle = 0
            center = self.head.center
            self.head_img = pygame.transform.rotate(self.head_img, angle)
            self.head = self.head_img.get_rect()
            self.head.center = center
            if angle:
                self.head_direction = direction
        if direction == "down":
            if self.head_direction == 'left':
                angle = 90
            elif self.head_direction == 'right':
                angle = -90
            else:
                angle = 0
            center = self.head.center
            self.head_img = pygame.transform.rotate(self.head_img, angle)
            self.head = self.head_img.get_rect()
            self.head.center = center
            if angle:
                self.head_direction = direction
        if direction == "left":
            if self.head_direction == 'up':
                angle = 90
            elif self.head_direction == 'down':
                angle = -90
            else:
                angle = 0
            center = self.head.center
            self.head_img = pygame.transform.rotate(self.head_img, angle)
            self.head = self.head_img.get_rect()
            self.head.center = center
            if angle:
                self.head_direction = direction
        if direction == "right":
            if self.head_direction == 'up':
                angle = -90
            elif self.head_direction == 'down':
                angle = 90
            else:
                angle = 0
            center = self.head.center
            self.head_img = pygame.transform.rotate(self.head_img, angle)
            self.head = self.head_img.get_rect()
            self.head.center = center
            if angle:
                self.head_direction = direction
    
    def turn_tail(self, direction):
        if direction == "down":
            if self.tail_direction == 'left':
                angle = 90
            elif self.tail_direction == 'right':
                angle = -90
            else:
                angle = 0
            center = self.tail.center
            self.tail_img = pygame.transform.rotate(self.tail_img, angle)
            self.tail = self.tail_img.get_rect()
            self.tail.center = center
            if angle:
                self.tail_direction = direction
        if direction == "up":
            if self.tail_direction == 'left':
                angle = -90
            elif self.tail_direction == 'right':
                angle = 90
            else:
                angle = 0
            center = self.tail.center
            self.tail_img = pygame.transform.rotate(self.tail_img, angle)
            self.tail = self.tail_img.get_rect()
            self.tail.center = center
            if angle:
                self.tail_direction = direction
        if direction == "right":
            if self.tail_direction == 'up':
                angle = -90
            elif self.tail_direction == 'down':
                angle = 90
            else:
                angle = 0
            center = self.tail.center
            self.tail_img = pygame.transform.rotate(self.tail_img, angle)
            self.tail = self.tail_img.get_rect()
            self.tail.center = center
            if angle:
                self.tail_direction = direction
        if direction == "left":
            if self.tail_direction == 'up':
                angle = 90
            elif self.tail_direction == 'down':
                angle = -90
            else:
                angle = 0
            center = self.tail.center
            self.tail_img = pygame.transform.rotate(self.tail_img, angle)
            self.tail = self.tail_img.get_rect()
            self.tail.center = center
            if angle:
                self.tail_direction = direction
    
    def move_head(self):
        if self.head_direction == 'left':
            self.head.x -= 1
        elif self.head_direction == 'right':
            self.head.x += 1
        elif self.head_direction == 'up':
            self.head.y -= 1
        elif self.head_direction == 'down':
            self.head.y += 1
        if self.head_direction == 'left' and self.head.left < 0:
            self.head.left = self.screen_rect.right
        elif self.head_direction == 'right' and self.head.left > self.screen_rect.right:
            self.head.left = 0
        elif self.head_direction == 'up' and self.head.top < 0:
            self.head.top = self.screen_rect.bottom
        elif self.head_direction == 'down' and self.head.top > self.screen_rect.bottom:
            self.head.top = 0
    
    def move_tail(self):
        if self.last_cell.direction != self.tail_direction:
            if self.tail.center == self.last_cell.turning_point:
                self.turn_tail(self.last_cell.direction)
        if self.tail_direction == 'left':
            self.tail.x -= 1
        elif self.tail_direction == 'right':
            self.tail.x += 1
        elif self.tail_direction == 'up':
            self.tail.y -= 1
        elif self.tail_direction == 'down':
            self.tail.y += 1
        if self.tail_direction == 'left' and self.tail.left < 0:
            self.tail.left = self.screen_rect.right
        elif self.tail_direction == 'right' and self.tail.left > self.screen_rect.right:
            self.tail.left = 0
        elif self.tail_direction == 'up' and self.tail.top < 0:
            self.tail.top = self.screen_rect.bottom
        elif self.tail_direction == 'down' and self.tail.top > self.screen_rect.bottom:
            self.tail.top = 0
    
    def grow(self):
        new_cell = Cell(self)
        self.cells.add(new_cell)
        self.last_cell = new_cell
        self.cell_count += 1
        self.tail.center = self.last_cell.rect.center
        if self.tail_direction == 'left':
            self.tail.left = self.last_cell.rect.right
        elif self.tail_direction == 'right':
            self.tail.right = self.last_cell.rect.left
        elif self.tail_direction == 'up':
            self.tail.top = self.last_cell.rect.bottom
        elif self.tail_direction == 'down':
            self.tail.bottom = self.last_cell.rect.top
    
    def move(self):
        self.move_head()
        for cell in self.cells.sprites():
            cell.move()
        self.move_tail()
        time.sleep(0.0015 / self.speed)
    
    def turn(self, direction):
        turn_time = time.time()
        if self.last_turn:
            if abs(turn_time - self.last_turn) < 0.125:
                return
        self.last_turn = turn_time
        self.turning_point = self.head.center
        self.turn_head(direction)
    
    def check(self):
        tail_x, tail_y = self.tail.center
        last_x, last_y = self.last_cell.rect.center
        dif_x, dif_y = abs(tail_x - last_x), abs(tail_y - last_y)
        need_repair = dif_x > self.last_cell.rect.width and dif_y > self.last_cell.rect.height
        if need_repair:
            self.repair_tail()
        head_x, head_y = self.head.center
        first_x, first_y = self.cells.sprites()[0].rect.center
        dif_x, dif_y = abs(head_x - first_x), abs(head_y - first_y)
        need_repair = dif_x > self.cells.sprites()[0].rect.width and dif_y > self.cells.sprites()[0].rect.height
        if need_repair:
            self.repair_head()
        self.manage_speed()
    
    def repair_head(self):
        self.head.center = self.cells.sprites()[0].rect.center
        self.turn_head(self.cells.sprites()[0].direction)
        if self.head_direction == 'right':
            self.head.left = self.cells.sprites()[0].rect.right
        elif self.head_direction == 'left':
            self.head.right = self.cells.sprites()[0].rect.left
        elif self.head_direction == 'down':
            self.head.top = self.cells.sprites()[0].rect.bottom
        elif self.head_direction == 'up':
            self.head.bottom = self.cells.sprites()[0].rect.top
    
    def repair_tail(self):
        self.tail.center = self.last_cell.rect.center
        self.turn_tail(self.last_cell.direction)
        if self.tail_direction == 'left':
            self.tail.left = self.last_cell.rect.right
        elif self.tail_direction == 'right':
            self.tail.right = self.last_cell.rect.left
        elif self.tail_direction == 'up':
            self.tail.top = self.last_cell.rect.bottom
        elif self.tail_direction == 'down':
            self.tail.bottom = self.last_cell.rect.top
    
    def manage_speed(self):
        self.speed = 1 + ((self.cell_count // 15) * 0.20)
    
    def draw(self):
        self.screen.blit(self.head_img, self.head)
        for cell in self.cells.sprites():
            cell.draw()
        self.screen.blit(self.tail_img, self.tail)

class Frog:
    
    def __init__(self, snack):
        self.hunter = snack
        self.screen = snack.screen
        self.screen_rect = self.screen.get_rect()
        self.img = pygame.image.load("src/images/frog.bmp")
        self.rect = self.img.get_rect()
        self.reappear()
    
    def reappear(self):
        x = random.randint(25, self.screen_rect.right - 15)
        y = random.randint(25, self.screen_rect.bottom - 15)
        self.rect.center = (x, y)
        if self.rect.collidelist([self.hunter.head, self.hunter.tail] + list(self.hunter.cells.sprites())) >= 0:
            self.reappear()
    
    def draw(self):
        self.screen.blit(self.img, self.rect)

class Text:
    
    def __init__(self, screen, text, font_size, text_color=(0, 0, 0), position='center', place="center", background=None, container=None):
        self.screen = screen
        self.font = pygame.font.SysFont(None, font_size)
        self.render_args = [text, True, text_color]
        self.text = text
        self.place = place
        if background:
            self.render_args.append(background)
        if type(container) is pygame.Rect:
            self.container = container
        else:
            self.container = screen.get_rect()
        if type(position) is str:
            self.position = self.container.center
        else:
            self.position = position
        self.render()
    
    def render(self):
        self.font_img = self.font.render(*self.render_args)
        self.rect = self.font_img.get_rect()
        if self.place == "right":
            x, y = self.position
            self.rect.right, self.rect.y = self.container.right - x, y
        elif self.place == "left":
            self.rect.x, self.rect.y = self.position
        else:
            self.rect.center = self.position
    
    def update_text(self, text):
        self.render_args[0] = text
        self.text = text
        self.render()
    
    def draw(self):
        self.screen.blit(self.font_img, self.rect)

class Button:
    
    def __init__(self, screen, width, height, background, position, text, fontsize=25, fontcolor=(0, 0, 0), onclick=None, place="center", shortcut=None):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, width, height)
        self.background = background
        self.position = position
        self.onclick = onclick
        self.shortcut = shortcut
        self.place = place
        self.exists = True
        if type(self.position) is str:
            self.position = self.screen_rect.center
        if self.place == "right":
            self.rect.right, self.rect.y = self.screen_rect.right - self.position[0], self.position[1]
        elif self.place == "left":
            self.rect.x, self.rect.y = self.position
        else:
            self.rect.center = self.position
        self.text = Text(self.screen, text, fontsize, fontcolor, container=self.rect)
    
    def check_event(self, event):
        if not self.onclick:
            return
        if (event.type == pygame.KEYDOWN and event.key in [pygame.K_KP_ENTER, pygame.K_SPACE]) or event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                self.onclick()
        elif self.shortcut:
            if event.type == pygame.KEYDOWN and event.key == self.shortcut:
                self.onclick()
    
    def draw(self):
        pygame.draw.rect(self.screen, self.background, self.rect)
        self.text.draw()
        