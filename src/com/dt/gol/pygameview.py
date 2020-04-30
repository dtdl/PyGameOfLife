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
    x_size = 120
    y_size = 80
    scale = 8
    SIZE = (x_size*scale, y_size*scale)

    """ start """
    pygame.init()
    WIN = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("game of life")
    
    w = World(x_size, y_size, x_size*y_size*0.5)
    
    for i in range(5000):
        
        for x in range(y_size):
            for y in range(x_size):
#                 print(f"(x:{x}, y:{y}): {w._cells[x][y]}")
                pygame.draw.rect(WIN,GREEN if w._cells[x][y] else BLACK, (y*scale, x*scale, scale, scale))
#                 pygame.display.update()
#             pygame.display.update()
        pygame.display.update()
        w.goNextGeneration()
        
        