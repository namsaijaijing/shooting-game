import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(x=x,y=y)

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
