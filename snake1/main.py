import pygame 
import random
import time
from Jablko import Jablko

SZEROKOSC_EKRANU = 800
WYSKOSC_EKRANU = 608

tlo = pygame.Surface((800,608))

# print(random.randrange(0,20))

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
        
        elif event.type == pygame.QUIT:
            gra_dziala = False

    ekran.blit(tlo, (0,0))

    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.pozycja)

    pygame.display.flip()

    zegar.tick(30)

time.sleep(1)

pygame.quit()