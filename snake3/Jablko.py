import pygame
import random


class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super(Jablko, self).__init__()
        self.obraz = pygame.image.load("images/apple.png")
        losowa_pozycja = pygame.Rect(random.randrange(1,25)*32, random.randrange(1,19)*32,32, 32)
        self.pozycja = losowa_pozycja
        self.rect = losowa_pozycja
