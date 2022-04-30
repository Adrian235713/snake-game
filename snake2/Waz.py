import pygame
from Direction import Direction
 
class Waz(pygame.sprite.Sprite):
    def __init__(self):
        self.oryginalny_obraz = pygame.image.load("images/head.png")
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)
        self.pozycja = self.obraz.get_rect(center=(12*32-16, 9*32-16))
 
        self.kierunek = Direction.GORA
        self.nowy_kierunek = Direction.GORA
 
    def zmine_kierunek(self, kierunek):
        zmiana_mozliwa = True
        if kierunek == Direction.GORA and self.kierunek == Direction.DOL:
            zmiana_mozliwa = False
        if kierunek == Direction.DOL and self.kierunek == Direction.GORA:
            zmiana_mozliwa = False
        if kierunek == Direction.LEWO and self.kierunek == Direction.PRAWO:
            zmiana_mozliwa = False
        if kierunek == Direction.PRAWO and self.kierunek == Direction.LEWO:
            zmiana_mozliwa = False
        if zmiana_mozliwa:
            self.nowy_kierunek = kierunek
 
    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz,(self.kierunek.value*-90))
        if self.kierunek == Direction.GORA:
            self.pozycja.move_ip(0, -32)
        if self.kierunek == Direction.PRAWO:
            self.pozycja.move_ip(32, 0)
        if self.kierunek == Direction.LEWO:
            self.pozycja.move_ip(-32, 0)
        if self.kierunek == Direction.DOL:
            self.pozycja.move_ip(0, 32)