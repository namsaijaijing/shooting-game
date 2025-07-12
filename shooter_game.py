#Create your own shooter
import pygame
import random
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
        self.enemy_group = pygame.sprite.Group()

        self.bullet_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        
        self.start_time = pygame.time.get_ticks()
        
        self.font1 = pygame.font.SysFont("Arial",24)
        self.font2 = pygame.font.SysFont("Arial",40)
        
        self.finish = False
        self.game_over = ""
        
    def run(self):
        running = True
        while(running):

            self.delta_time = self.clock.tick(60)/1000
            current_time = pygame.time.get_ticks()
            elapsed_time = ( current_time - self.start_time ) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.BG, (0,0))
            if self.finish == False:
                self.result()
                bullet = self.player.move(self.delta_time)
                if(bullet != None):
                    self.bullet_group.add(bullet)
                self.bullet_group.draw(self.screen)
                self.bullet_group.update()
                self.player.draw(self.screen)
                if elapsed_time > 1 :
                    self.enemy_group.add(Enemy(random.randint(0,600),0,self.enemy_image))
                    self.start_time = current_time
                self.enemy_group.draw(self.screen)
                self.enemy_group.update(self.player)
                print(self.enemy_group)
                self.shooting()
                print(self.player.score)
                self.player_shooted()
                print(self.player.health)
                
                self.display_text()
                
                self.player.check_adge()
            else:
                self.end_game()
                
            pygame.display.update()
            

        pygame.quit()

    def shooting(self):
        for bullet in self.bullet_group:
            for enemy in self.enemy_group:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.kill()
                    bullet.kill()
                    self.player.score += 1
                    
    def player_shooted(self):
        for enemy in self.enemy_group:
            if enemy.rect.colliderect(self.player.rect):
                self.player.health -= 1
                enemy.kill()
                
    def display_text(self):
        score_text = self.font1.render("SCORE: "+str(self.player.score),True,(255,255,255))
        self.screen.blit(score_text,(10,10))
        health_text = self.font1.render("HEALTH: "+str(self.player.health),True,(255,255,255))
        self.screen.blit(health_text,(10,40))
    
    def end_game(self):
        if self.game_over == 'WIN':
            win_text = self.font2.render("YOU WIN!!",True,(255,255,255))
            self.screen.blit(win_text,(320,220))
        if self.game_over == 'LOSE':
            lose_text = self.font2.render("YOU LOSE!!",True,(255,255,255))
            self.screen.blit(lose_text,(320,220))
        
    def result(self):
        if self.player.score == 10:
            self.finish = True
            self.game_over = "WIN"
        if self.player.health == 0:
            self.finish = True
            self.game_over = "LOSE"
             
                
                
    

game = Game()
game.run()