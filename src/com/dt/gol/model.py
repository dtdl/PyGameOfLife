'''
Created on Apr 30, 2020

@author: GoldenSource
'''

from numpy.random.mtrand import randint

class Cell(object):
    '''
    classdocs
    '''

    __alive = None

    def __init__(self, alive):
        '''
        Constructor
        '''
        
        self.__alive = alive
        


class World(object):
    '''
    classdocs
    '''

    __x_size = None
    __y_size = None
    __cell_cnt = None
    
    __cells = None
    
    __generation = 0

    def __init__(self, x, y, cnt):
        '''
        Constructor
        '''
        
        self.__x_size = x
        self.__y_size = y
        self.__cell_cnt = cnt
        self.__initialCells()
        
    
    def __initialCells(self):
        
        cells = []
        
        for j in range(self.__y_size):
            x_cells = []
            for i in range(self.__x_size):
#                 cell = Cell(True if randint(0, 1) == 0 else False);
                cell = True if randint(0, 2) == 0 else False
                x_cells.append(cell)
                
#             print(x_cells)
            cells.append(x_cells)
            
        self.__cells = cells
    
    
    
    def goNextGeneration(self):

        
        
        self.__generation += 1
        
        return None
    
    def show(self):
        print(self.__x_size)
        print(self.__y_size)
        print(self.__generation)
        print(self.__cell_cnt)
        print(self.__cells)
        

        
if __name__ == '__main__':
    pass
   
#     print(help(World))
    w = World(10, 10, 5)
    w.show()
    w.goNextGeneration()
    w.show()

     
