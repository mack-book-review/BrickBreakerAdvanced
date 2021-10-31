import pygame
from constants import *

class Brick():

    def __init__(self,xPos,yPos,width,height,color, health = 1):
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(xPos,yPos,width,height)
        self.isDead = False
        self.health = health
        self.isColliding = False

        self.collisionTimer = 0
        self.collisionDebounceInterval = 1000
        self.prev_ticks = 0
        self.current_ticks = 0


    def takeDamage(self):
        if not self.isColliding:
            self.isColliding = True
            self.collisionTimer = 0
            self.health -= 1
            print("Took damage: " +str(self.health))
            if self.health <= 0:
                self.isDead = True

    def kill(self):
        self.isDead = True

    def draw(self,screen):
        if not self.isDead:
            pygame.draw.rect(screen,self.color,(self.rect.x,self.rect.y,self.width,self.height))

    def update(self):
        self.current_ticks = pygame.time.get_ticks()
        elapsed_ticks = self.current_ticks - self.prev_ticks

        self.collisionTimer += elapsed_ticks

        if self.collisionTimer > self.collisionDebounceInterval:
            self.isColliding = False
            self.collisionTimer = 0

        self.current_ticks = 0

        self.prev_ticks = self.current_ticks