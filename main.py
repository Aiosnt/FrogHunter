import pygame
from src.python import homescreen


pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Frog Hunter")
homescreen.main(screen)

"""Project: Frog Hunter
Author: Rajin Alim
Completed On Saturday, 17 October 2020 7:10 PM"""