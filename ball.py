import pygame
from constants import *

class Ball():

    def __init__(self,width = BALL_WIDTH,height = BALL_HEIGHT, color = LIGHT_BLUE):
        self.width = width
        self.height = height
        self.color = color
        self.x = SCREEN_WIDTH*0.5
        self.y = SCREEN_HEIGHT-self.height*1.5
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

        self.prev_ticks = 0
        self.current_ticks = 0
        self.elapsed_ticks = 0
        self.moveTimer = 0
        self.moveInterval = 2000

        self.old_pos = (self.x,self.y)
        self.new_pos = (self.x,self.y)

        self.isMovingUp = True
        self.isMovingRight = True

        #start intial movement
        self.moveUp()
        self.moveRight()

    def lerp(self, old_pos, new_pos, percent):
        if old_pos and new_pos:
            dist_x = (new_pos[0] - old_pos[0]) * percent
            dist_y = (new_pos[1] - old_pos[1]) * percent
            self.rect.x = old_pos[0] + dist_x
            self.rect.y = old_pos[1] + dist_y

    def draw(self,screen):
        pygame.draw.ellipse(screen,self.color,self.rect)



    def moveRight(self):
        self.moveTimer = 0
        self.old_pos = (self.rect.x, self.rect.y)
        self.new_pos = (SCREEN_WIDTH+50, self.new_pos[1])

    def moveLeft(self):
        self.moveTimer = 0
        self.old_pos = (self.rect.x, self.rect.y)
        self.new_pos = (-50, self.new_pos[1])

    def moveUp(self):
        self.moveTimer = 0
        self.old_pos = (self.rect.x, self.rect.y)
        self.new_pos = (self.new_pos[0], -50)

    def moveDown(self):
        self.moveTimer = 0
        self.old_pos = (self.rect.x, self.rect.y)
        self.new_pos = (self.new_pos[0], SCREEN_HEIGHT+50)

    def update(self):


        if self.rect.x <= 0:
            self.moveRight()

        if self.rect.x >= SCREEN_WIDTH - self.width:
            self.moveLeft()

        if self.rect.y <= 0:
            self.moveDown()

        if self.rect.y >= SCREEN_HEIGHT - self.height:
            self.moveUp()

        self.current_ticks = pygame.time.get_ticks()
        self.elapsed_ticks = self.current_ticks - self.prev_ticks


        self.moveTimer += self.elapsed_ticks
        percent = self.moveTimer / self.moveInterval
        self.lerp(self.old_pos, self.new_pos, percent)

        if self.moveTimer >= self.moveInterval:
            self.moveTimer = 0
            self.old_pos = self.new_pos
            self.new_pos = None

        self.prev_ticks = self.current_ticks