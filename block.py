import sys
sys.path.append("C:\Python36\Lib\site-packages")
import pygame
import random
from pygame.sprite import Sprite

class Block(Sprite):
    def __init__(self,settings,screen):
        super(Block,self).__init__()
        self.choice = random.randint(1,10)
        self.screen = screen
        if self.choice == 1 :
            self.image = pygame.image.load('images/blue.png')
        elif self.choice == 2 :
            self.image = pygame.image.load('images/aqua.png')
        elif self.choice == 3 :
            self.image = pygame.image.load('images/brown.png')
        elif self.choice == 4 :
            self.image = pygame.image.load('images/green.png')
        elif self.choice == 5 :
            self.image = pygame.image.load('images/lime.png')
        elif self.choice == 6 :
            self.image = pygame.image.load('images/orange.png')
        elif self.choice == 7 :
            self.image = pygame.image.load('images/pink.png')
        elif self.choice == 8 :
            self.image = pygame.image.load('images/purple.png')
        elif self.choice == 9 :
            self.image = pygame.image.load('images/red.png')
        elif self.choice == 10 :
            self.image = pygame.image.load('images/yellow.png')

        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image,self.rect)
            


        
