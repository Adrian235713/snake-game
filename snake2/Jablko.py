import pygame
import random

# Creating a sprite
# Now we’re ready to make our first sprite. In Pygame, sprites are objects. 
# If you haven’t worked with objects in Python before, they are a convenient way of grouping data and 
# code into a single entity. It may be a little confusing at first, but fortunately, Pygame sprites are a
# good way to practice with objects and get used to how they work.

# We start by defining our new sprite
# lass Player(pygame.sprite.Sprite):

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super(Jablko, self).__init__()
        self.obraz = pygame.image.load("images/apple.png")
        losowa_pozycja = pygame.Rect(random.randrange(1,25)*32, random.randrange(1,19)*32,32, 32)
        self.pozycja = losowa_pozycja
