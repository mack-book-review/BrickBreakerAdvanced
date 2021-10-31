from brick import Brick
from constants import *

class BrickGroup():


    def __init__(self,rows,cols):
        self.target_bricks = []
        self.target_rects = []
        self.killCount = 0
        self.num_rows = rows
        self.num_cols = cols
        x_margin_space = 50
        brick_width = (SCREEN_WIDTH - x_margin_space - 10) / self.num_cols
        x_offset = x_margin_space / self.num_cols

        y_margin_space = 50
        brick_height = (SCREEN_WIDTH / 4 - y_margin_space - 10) / self.num_rows
        y_offset = y_margin_space / self.num_cols

        x_pos = 0
        y_pos = 0

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x_pos = 10 + (x_offset + brick_width) * col
                y_pos = 10 + (y_offset + brick_height) * row
                b = Brick(x_pos, y_pos, brick_width, brick_height, FOREST_GREEN,2)
                self.target_bricks.append(b)
                self.target_rects.append(b.rect)

    #Unnecessary if using the update method
    def draw(self,screen):
        for b in self.target_bricks:
            b.update()
            if not b.isDead:
                b.draw(screen)

    #Unnecessary if using the update method
    def testForCollisions(self,ball):
        index_collide = ball.rect.collidelist(self.target_rects)
        if index_collide != -1 and not self.target_bricks[index_collide].isDead:
            if ball.rect.top <= self.target_bricks[index_collide].rect.bottom:
                ball.moveDown()
                self.target_bricks[index_collide].takeDamage()
                if self.target_bricks[index_collide].isDead:
                    self.killCount += 1

    def totalBricks(self):
        return self.num_rows*self.num_cols


    def update(self,screen,ball):
        for b in self.target_bricks:
            b.update()
            if b.rect.colliderect(ball.rect) and not b.isDead:
                if ball.rect.top <= b.rect.bottom:
                    ball.moveDown()
                    b.takeDamage()
                    if b.isDead:
                        self.killCount += 1

            b.draw(screen)