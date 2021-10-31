import pygame

from brick import Brick
from constants import *


class Player(Brick):

    def __init__(self):
        super().__init__(SCREEN_WIDTH*0.5,SCREEN_HEIGHT-PLAYER_HEIGHT*1.5, PLAYER_WIDTH,PLAYER_HEIGHT,TOMATO_RED)
        self.prev_ticks = 0
        self.current_ticks = 0
        self.elapsed_ticks = 0
        self.isMoving = False
        self.isMovingLeft = False
        self.isMovingRight = False
        self.moveTimer = 0
        self.moveInterval = 2000

        self.old_pos = (self.rect.x, self.rect.y)
        self.new_pos = None

    def update(self):
        super.update()

    def lerp(self, old_pos, new_pos, percent):
        if old_pos and new_pos:
            dist_x = (new_pos[0] - old_pos[0]) * percent
            dist_y = (new_pos[1] - old_pos[1]) * percent
            self.rect.x = old_pos[0] + dist_x
            self.rect.y = old_pos[1] + dist_y

    def moveLeft(self):
        if not self.isMovingLeft:
            self.moveTimer = 0
            self.isMovingLeft = True
            self.isMovingRight = False
            self.isMoving = True
            self.old_pos = (self.rect.x, self.rect.y)
            self.new_pos = (-50, self.rect.y)

    def moveRight(self):
        if not self.isMovingRight:
            self.moveTimer = 0
            self.isMovingRight = True
            self.isMovingLeft = False
            self.isMoving = True
            self.old_pos = (self.rect.x, self.rect.y)
            self.new_pos = (SCREEN_WIDTH + 50, self.rect.y)

    def update(self):
        # self.updateCoordinates()
        if self.rect.x <= 0:
            self.moveRight()

        if self.rect.x >= SCREEN_WIDTH - self.width:
            self.moveLeft()

        self.current_ticks = pygame.time.get_ticks()
        self.elapsed_ticks = self.current_ticks - self.prev_ticks

        if self.isMoving:
            self.moveTimer += self.elapsed_ticks
            percent = self.moveTimer / self.moveInterval
            self.lerp(self.old_pos, self.new_pos, percent)

            if self.moveTimer >= self.moveInterval:
                self.moveTimer = 0
                self.isMoving = False
                self.old_pos = self.new_pos
                self.new_pos = None

        self.prev_ticks = self.current_ticks