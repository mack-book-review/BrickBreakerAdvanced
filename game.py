import pygame,sys
from player import Player
from ball import Ball
from brick import Brick
from brick_group import BrickGroup
from constants import *

class Game(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 500))
        pygame.display.set_caption("Brick Breaker")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.ball = Ball()
        self.brickGroup = BrickGroup(1,3)
        self.gameLost = False
        self.gameWon = False

    def handleInput(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    self.player.moveRight()

    def run(self):

        while not self.gameLost and not self.gameWon:
            self.screen.fill((255, 255, 255))

            self.handleInput(pygame.event.get())

            self.player.draw(self.screen)
            self.player.update()

            #self.brickGroup.testForCollisions(self.ball)
            #self.brickGroup.draw(self.screen)

            self.brickGroup.update(self.screen,self.ball)
            self.ball.draw(self.screen)
            self.ball.update()

            if self.ball.rect.bottom >= SCREEN_HEIGHT:
                self.gameLost = True

            if self.ball.rect.colliderect(self.player.rect):
                if self.ball.rect.bottom >= self.player.rect.top:
                    self.ball.moveUp()

            if self.brickGroup.killCount >= self.brickGroup.totalBricks():
                self.gameWon = True

            pygame.display.flip()
            self.clock.tick(60)

        if self.gameWon:
            print("You won!")

        if self.gameLost:
            print("You lost!")