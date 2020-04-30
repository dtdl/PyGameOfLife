'''
Created on Apr 30, 2020

@author: GoldenSource
'''
import pygame
from com.dt.gol.model import World

if __name__ == '__main__':
    pass
    
    """ collor """
#     WHITE   = (255,255,255)
#     RED     = (255, 0, 0)
    GREEN   = (0, 255, 220)
    BLACK   = (0, 0, 0)

    """ size of the world, scale of the view """
    size = 120
    scale = 3
    SIZE = (size*scale, size*scale)

    """ start """
    pygame.init()
    WIN = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("game of life")
    
    w = World(size, size, size*size*0.2)
    
    for i in range(2000):
        
        for x in range(size):
            for y in range(size):
                pygame.draw.rect(WIN,GREEN if w._cells[x][y] else BLACK, (x*scale, y*scale, scale, scale))
#                 pygame.display.update()
#             pygame.display.update()
        pygame.display.update()
        w.goNextGeneration()
        
        