import pygame
from player import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(x=x,y=y)

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
    def update(self,player):
        self.rect.y += 1
        self.check(player)
        
    def check(self,player):
        if self.rect.y > 500 :
            self.kill()
            player.health -=1
