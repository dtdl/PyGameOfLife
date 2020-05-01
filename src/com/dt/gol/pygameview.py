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
    x_size = 100
    y_size = 60
    scale = 8
    cell_rate = 0.1
    generation = 10000
    
    SIZE = (x_size*scale, y_size*scale)

    """ start """
    pygame.init()
    WIN = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("game of life")
    
    w = World(x_size, y_size, x_size*y_size*cell_rate)
    
    for i in range(generation):
        
        for x in range(x_size):
            for y in range(y_size):
#                 print(f"(x:{x}, y:{y}): {w._cells[y][x]}")
                pygame.draw.rect(WIN, GREEN if w._cells[y][x] else BLACK, (x*scale, y*scale, scale, scale))
#                 pygame.display.update()
#             pygame.display.update()
        pygame.display.update()
        w.goNextGeneration()
        
        