import pygame

class Draw:
    def __init__(self):
        pass
    def drawCircle(self,screen,color,center,radius):
        pygame.draw.circle(screen,color,center,radius)
        