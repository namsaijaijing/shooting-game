import pygame
from bullet import *

class Player():
    def __init__(self,x,y,image,bullet_image):
        self.image = image
        self.bullet_image = bullet_image
        self.rect = image.get_rect(x=x,y=y)
        self.x_pos = float(x)
        self.speed = 200
        self.fired = False
        self.start_time = pygame.time.get_ticks()
        
        self.health = 3
        self.score = 0


    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def move(self,delta_time):
        pressed = pygame.key.get_pressed()
        dx = 0
        if pressed[pygame.K_LEFT]:
            dx = -1
        if pressed[pygame.K_RIGHT]:
            dx = 1
        current_time = pygame.time.get_ticks()
        if (current_time - self.start_time > 500):
            self.fired = False
        if pressed[pygame.K_SPACE] and not self.fired:
            self.fired = True
            self.start_time = current_time
            return Bullet((self.rect.x+self.rect.w/2)-(self.bullet_image.get_width()/2),self.rect.y,self.bullet_image)

        self.x_pos += dx * self.speed * delta_time
        self.rect.x = int(self.x_pos)
    
    def check_adge(self):
        if self.rect.x <= 0:
            self.rect.x = 0
            self.x_pos = float(self.rect.x)
        if self.rect.x >= (700-self.rect.w):
            self.rect.x = (700-self.rect.w)
            self.x_pos = float(self.rect.x)
        