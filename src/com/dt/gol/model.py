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

    __cells = None

    __cell_cnt = 0
    __generation = 0

    def __init__(self, x, y, cnt):
        '''
        Constructor
        '''
        
        self.__x_size = x
        self.__y_size = y
#         self.__cell_cnt = cnt
        self.__initialCells(cnt)
        
    
    def __initialCells(self, cnt):
        
        cells = []
        
        for j in range(self.__y_size):
            x_cells = []
            for i in range(self.__x_size):
#                 cell = Cell(True if randint(0, 1) == 0 else False);
#                 cell = True if randint(0, 2) == 0 else False
                cell = 1 if randint(0, self.__x_size * self.__y_size - 1) < cnt else 0
                if cell:
                    self.__cell_cnt += 1
                
                x_cells.append(cell)
                
#             print(x_cells)
            cells.append(x_cells)
            
        self.__cells = cells
    
    def getNeighbourCnt(self, x, y) -> int:
        
        xl = x+1 if x+1 < self.__x_size else 0
        yl = y+1 if y+1 < self.__y_size else 0 

#         print(f"({x-1}, {y-1}) = {self.__cells[x-1][y-1]}")
#         print(f"({x-1}, {y}) = {self.__cells[x-1][y]}")
#         print(f"({x-1}, {yl}) = {self.__cells[x-1][yl]}")
#         print(f"({x}, {y-1}) = {self.__cells[x][y-1]}")
###         print(f"({x}, {y}) = {self.__cells[x][y]}")
#         print(f"({x}, {yl}) = {self.__cells[x][yl]}")
#         print(f"({xl}, {y-1}) = {self.__cells[xl][y-1]}")
#         print(f"({xl}, {y}) = {self.__cells[xl][y]}")
#         print(f"({xl}, {yl}) = {self.__cells[xl][yl]}")
        
        return self.__cells[x-1][y-1] + self.__cells[x-1][y] + self.__cells[x-1][yl] + self.__cells[x][y-1] + self.__cells[x][yl] + self.__cells[xl][y-1] + self.__cells[xl][y] + self.__cells[xl][yl]
    
    def goNextGeneration(self):

        cells = []
        cell_cnt = 0
        
        for i in range(self.__y_size):
            x_cells = []
            for j in range(self.__x_size):
#                 print(f"({i}, {j}) = {self.__cells[i][j]}")
                nbcnt = self.getNeighbourCnt(i, j)
                cell = None
#                 print(nbcnt)
                
                if nbcnt == 3:
                    cell = 1
                elif nbcnt == 2:
                    cell = self.__cells[i][j]
                else:
                    cell = 0
                 
                if cell:
                    cell_cnt += 1
                
                x_cells.append(cell)
                
#             print(x_cells)
            cells.append(x_cells)
            
        self.__cells = cells
        self.__cell_cnt = cell_cnt
        self.__generation += 1

        self.show()


    
    def show(self):
#         print(self.__x_size)
#         print(self.__y_size)
        print(f'genration: {self.__generation}')
        print(self.__cell_cnt)
        print(self.__cells)
        

        
if __name__ == '__main__':
    pass
   
#     print(help(World))
    w = World(20, 20, 110)
    w.show()
    for i in range(310):
        w.goNextGeneration()
    
#     w.show()
#     for i in range(100):
#         print (randint(0, 10 * 10))
     
