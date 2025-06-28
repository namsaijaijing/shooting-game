import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(x=x,y=y)

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y -= 1
        self.check()

    def check(self):
        if self.rect.y < 0 :
            self.kill()