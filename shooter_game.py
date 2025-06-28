#Create your own shooter
import pygame
from player import *
from enemy import *


class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700,500))
        pygame.display.set_caption("SHOOTING GAME")

        self.BG = pygame.image.load("galaxy.jpg")
        self.BG = pygame.transform.scale(self.BG,(700,500))

        self.bullet_image = pygame.image.load("bullet.png")
        self.bullet_image = pygame.transform.scale(self.bullet_image,(640/25,1280/25))

        self.player_image = pygame.image.load("rocket.png")
        self.player_image = pygame.transform.scale(self.player_image,(1302/16,1920/16))
        self.player = Player(300,375,self.player_image,self.bullet_image)

        self.enemy_image = pygame.image.load("ufo.png")
        self.enemy_image = pygame.transform.scale(self.enemy_image,(1280/12,649/12))
        self.enemy = Enemy(400,375,self.enemy_image)

        self.bullet_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
    def run(self):
        running = True
        while(running):

            self.delta_time = self.clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.BG, (0,0))
            bullet = self.player.move(self.delta_time)
            if(bullet != None):
                self.bullet_group.add(bullet)
                print(self.bullet_group)
            self.bullet_group.draw(self.screen)
            self.bullet_group.update()
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)
            
            self.player.check_adge()
            pygame.display.update()

        pygame.quit()

    

game = Game()
game.run()