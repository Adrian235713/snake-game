import pygame
from Direction import Direction
from Segment import Segment
import copy
 
class Waz(pygame.sprite.Sprite):
    def __init__(self):
        self.oryginalny_obraz = pygame.image.load("images/head.png")
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)
        self.pozycja = self.obraz.get_rect(center=(12*32-16, 9*32-16))
 
        self.kierunek = Direction.GORA
        self.nowy_kierunek = Direction.GORA

        self.rect = self.pozycja #oki  wiem...
        self.ostatnia_pozycja = self.pozycja
        self.dodaj_segment = False
        self.segmenty = []
 
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
 
    #  ------------------------------------------33333333333333
    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz,(self.kierunek.value*-90))


        self.ostatnia_pozycja = copy.deepcopy(self.pozycja)

        if self.kierunek == Direction.GORA:
            self.pozycja.move_ip(0, -32)
        if self.kierunek == Direction.PRAWO:
            self.pozycja.move_ip(32, 0)
        if self.kierunek == Direction.LEWO:
            self.pozycja.move_ip(-32, 0)
        if self.kierunek == Direction.DOL:
            self.pozycja.move_ip(0, 32)

        for i in range(len(self.segmenty)):
            if i == 0:
                self.segmenty[i].przesun(self.ostatnia_pozycja)
            else:
                self.segmenty[i].przesun(self.segmenty[i-1].ostatnia_pozycja)

        if self.dodaj_segment:
            nowy_segment = Segment()
 
            nowa_pozycja = None
            if len(self.segmenty) > 0:
                nowa_pozycja = copy.deepcopy(self.segmenty[-1].pozycja)
            else:
                nowa_pozycja = copy.deepcopy(self.ostatnia_pozycja)
                nowy_segment.pozycja = nowa_pozycja
            self.segmenty.append(nowy_segment)
            self.dodaj_segment = False


    #  ------------------------------------------33333333333333
    
    def sprawdz_kolizje(self):
        for segment in self.segmenty:
            if self.rect.topleft == segment.pozycja.topleft:
                return True
 
        if self.rect.top < 0 or self.rect.top >= 608:
            return True
        if self.rect.left < 0 or self.rect.left >= 800:
            return True
        
        return False

    #  ------------------------------------------33333333333333

    def rysuj_segmenty(self, ekran):
        for segment in self.segmenty:
            ekran.blit(segment.obraz, segment.pozycja)
 
    def jedz_jablko(self):
        self.dodaj_segment = True