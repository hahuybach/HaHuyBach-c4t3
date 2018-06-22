import pygame
import random
from pygame.locals import *
width = 400
height = 400
display_surf = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
GREEN = (255,255,255)

fps = 250
fps_clock = pygame.time.Clock()

class Snake:
    def __init__(self,r,x,y):
        self.r = r
        self.x = x
        self.y = y
    def Draw(self):
        pygame.draw.circle(display_surf,GREEN,(self.x,self.y,self.r,self.r))
    def move(self,pos):
        self.x = self.x + pos[0]
        self.y = self.y + pos[1]

class Food:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Draw(self):
        pygame.draw.circle(display_surf,RED,(self.x,self.y))#em không biết dùng cái random như nào
class Game:
    def hit_the_ceiling(self):
        if self.y == 0:
            return True
        else:
            return False
    def hit_the_floor(self):
        if self.y == height:
            return True
        else:
            return False
    def hit_the_edge(self):
        if self.x == 0 or self.x == width:
            return True
        else:
            return False
    def snake_eat_food(self,Food):
        if self.x == Food.x and self.y == Food.y:
            #rắn dài ra
    def snake_eat_snake(self):
        #end game
