import pygame
import random
import time
from Jablko import Jablko
from Direction import Direction
from Waz import Waz
 
SZEROKOSC_EKRANU = 800
WYSKOSC_EKRANU = 608
 
tlo = pygame.Surface((800,608))
 
 
for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0,20),random.randrange(0,20),random.randrange(0,20))
        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i*32, j*32))
 
# ----------------------------------------------------
 
pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU,WYSKOSC_EKRANU])
zegar = pygame.time.Clock()
 
# ----------------------------------------------------
waz = Waz()
PORUSZANIE_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZANIE_WEZEM, 200)
 
# ----------------------------------------------------
jablko = Jablko()
#A container class to hold and manage multiple Sprite objects.
jablka = pygame.sprite.Group()
jablka.add(jablko)
 
# ----------------------------------------------------
 
gra_dziala = True
while gra_dziala:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gra_dziala = False
            # ----------------------------------------------------
            #Sterowanie
 
            if event.key == pygame.K_w:
                waz.zmine_kierunek(Direction.GORA)
            if event.key == pygame.K_s:
                waz.zmine_kierunek(Direction.DOL)
            if event.key == pygame.K_a:
                waz.zmine_kierunek(Direction.LEWO)
            if event.key == pygame.K_d:
                waz.zmine_kierunek(Direction.PRAWO)
 
            # ----------------------------------------------------
        elif event.type == pygame.QUIT:
            gra_dziala = False
 
        elif event.type == PORUSZANIE_WEZEM:
            waz.aktualizuj()


    # ----------33333333333333333333333333
    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka)
    if kolizja_z_jablkiem != None:
        kolizja_z_jablkiem.kill()
        waz.jedz_jablko()
        jablko = Jablko()
        jablka.add(jablko)

    # ----------33333333333333333333333333
           
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.pozycja)


    if waz.sprawdz_kolizje():
        gra_dziala = False
 
    pygame.display.flip()
 
 
    ekran.blit(tlo, (0,0))
    # ----------33333333333333333333333333
    waz.rysuj_segmenty(ekran)
    # ----------33333333333333333333333333

    ekran.blit(waz.obraz, waz.pozycja)
    zegar.tick(30)
 
time.sleep(1)
 
pygame.quit()
