import numpy as np 
import random

MAP_GROUND = 0
MAP_WALL = -1
MAP_POINT = 1
MAP_TARGET = 2

class MazeMaker:
    def __init__(self,method='backtracker'):
        self.method = method

    def __backtracker(self,shape,startposition):
        '''
        Recursive backtracker
        '''
        (num_rows,num_cols) = shape
        M = np.zeros((num_rows,num_cols,5), dtype=np.uint8)

        (r,c) = startposition
        history = [startposition]

        while history:   
            M[r,c,4] = 1    # Visited?
            check = []  
            if c > 0 and M[r,c-1,4] == 0:  
                check.append('L')    
            if r > 0 and M[r-1,c,4] == 0:  
                check.append('U')  
            if c < num_cols-1 and M[r,c+1,4] == 0:  
                check.append('R')  
            if r < num_rows-1 and M[r+1,c,4] == 0:  
                check.append('D')      
            
            if len(check):  
                history.append([r,c])  
                move_direction = random.choice(check)  
                if move_direction == 'L':  
                    M[r,c,0] = 1            # Connected?
                    c = c-1  
                    M[r,c,2] = 1  
                if move_direction == 'U':  
                    M[r,c,1] = 1  
                    r = r-1  
                    M[r,c,3] = 1  
                if move_direction == 'R':  
                    M[r,c,2] = 1  
                    c = c+1  
                    M[r,c,0] = 1  
                if move_direction == 'D':  
                    M[r,c,3] = 1  
                    r = r+1  
                    M[r,c,1] = 1  
            else:  
                r,c = history.pop()  
        
        return M

    def __prim(self,shape,startposition):
        '''
        Randomized Prim's algorithm
        '''
        (num_rows,num_cols) = shape
        M = np.zeros((num_rows,num_cols,5), dtype=np.uint8)

        (r,c) = startposition
        history = [startposition]

        while history:     
            r,c = random.choice(history)  
            M[r,c,4] = 1 # designate this location as visited  
            history.remove((r,c))  
            check = []  
               
            if c > 0:  
                if M[r,c-1,4] == 1:  
                    check.append('L')  
                elif M[r,c-1,4] == 0:  
                    history.append((r,c-1))  
                    M[r,c-1,4] = 2  
            if r > 0:  
                if M[r-1,c,4] == 1:   
                    check.append('U')   
                elif M[r-1,c,4] == 0:  
                    history.append((r-1,c))  
                    M[r-1,c,4] = 2  
            if c < num_cols-1:  
                if M[r,c+1,4] == 1:   
                    check.append('R')  
                elif M[r,c+1,4] == 0:  
                    history.append((r,c+1))  
                    M[r,c+1,4] = 2   
            if r < num_rows-1:  
                if M[r+1,c,4] == 1:   
                    check.append('D')   
                elif  M[r+1,c,4] == 0:  
                    history.append((r+1,c))  
                    M[r+1,c,4] = 2  
        
            # select one of these edges at random.  
            if len(check):  
                move_direction = random.choice(check)  
                if move_direction == 'L':  
                    M[r,c,0] = 1  
                    c = c-1  
                    M[r,c,2] = 1  
                if move_direction == 'U':  
                    M[r,c,1] = 1  
                    r = r-1  
                    M[r,c,3] = 1  
                if move_direction == 'R':  
                    M[r,c,2] = 1  
                    c = c+1  
                    M[r,c,0] = 1  
                if move_direction == 'D':  
                    M[r,c,3] = 1  
                    r = r+1  
                    M[r,c,1] = 1  
           
        
        M[0,0,0] = 1  
        M[num_rows-1,num_cols-1,2] = 1  
                
        return M

    def __division(self,shape,startposition):
        '''
        Recursive division
        '''
        (num_rows,num_cols) = shape
        M = np.zeros((num_rows,num_cols,5), dtype=np.uint8)

        (r,c) = startposition
        history = [startposition]

        r1 = 0  
        r2 = num_rows-1  
        c1 = 0  
        c2 = num_cols-1     

        self.__Recursive_division(r1, r2, c1, c2, M)

        M[0,0,0] = 1  
        M[num_rows-1,num_cols-1,2] = 1  

        return M

    def __Recursive_division(self,r1, r2, c1, c2, M):  
        if r1 < r2 and c1 < c2:  
            rm = random.randint(r1, r2-1)  
            cm = random.randint(c1, c2-1)  
            cd1 = random.randint(c1,cm)  
            cd2 = random.randint(cm+1,c2)  
            rd1 = random.randint(r1,rm)  
            rd2 = random.randint(rm+1,r2)  
            d = random.randint(1,4)  
            if d == 1:  
                M[rd2, cm, 2] = 1  
                M[rd2, cm+1, 0] = 1  
                M[rm, cd1, 3] = 1  
                M[rm+1, cd1, 1] = 1  
                M[rm, cd2, 3] = 1  
                M[rm+1, cd2, 1] = 1  
            elif d == 2:  
                M[rd1, cm, 2] = 1  
                M[rd1, cm+1, 0] = 1  
                M[rm, cd1, 3] = 1  
                M[rm+1, cd1, 1] = 1  
                M[rm, cd2, 3] = 1  
                M[rm+1, cd2, 1] = 1  
            elif d == 3:  
                M[rd1, cm, 2] = 1  
                M[rd1, cm+1, 0] = 1  
                M[rd2, cm, 2] = 1  
                M[rd2, cm+1, 0] = 1  
                M[rm, cd2, 3] = 1  
                M[rm+1, cd2, 1] = 1  
            elif d == 4:  
                M[rd1, cm, 2] = 1  
                M[rd1, cm+1, 0] = 1  
                M[rd2, cm, 2] = 1  
                M[rd2, cm+1, 0] = 1  
                M[rm, cd1, 3] = 1  
                M[rm+1, cd1, 1] = 1  
    
            self.__Recursive_division(r1, rm, c1, cm, M)  
            self.__Recursive_division(r1, rm, cm+1, c2, M)  
            self.__Recursive_division(rm+1, r2, cm+1, c2, M)  
            self.__Recursive_division(rm+1, r2, c1, cm, M)  
    
        elif r1 < r2:  
            rm = random.randint(r1, r2-1)  
            M[rm,c1,3] = 1  
            M[rm+1,c1,1] = 1  
            self.__Recursive_division(r1, rm, c1, c1, M)  
            self.__Recursive_division(rm+1, r2, c1, c1, M)  
        elif c1 < c2:  
            cm = random.randint(c1,c2-1)  
            M[r1,cm,2] = 1  
            M[r1,cm+1,0] = 1  
            self.__Recursive_division(r1, r1, c1, cm, M)  
            self.__Recursive_division(r1, r1, cm+1, c2, M)  

    def __transform(self,M,shape,startposition):
        (num_rows,num_cols) = shape

        maze = np.zeros((2*num_rows-1, 2*num_cols-1))
        maze[startposition] = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if (M[i,j,2] == 0) and (2*j + 1 < 2*num_cols - 1):
                    maze[2*i,2*j+1] = MAP_WALL
                if (M[i,j,1] == 0) and (2*i - 1 >= 0):
                    maze[2*i-1,2*j] = MAP_WALL
                if (M[i,j,0] == 0) and (2*j - 1 >= 0):
                    maze[2*i,2*j-1] = MAP_WALL
                if (M[i,j,3] == 0) and (2*i + 1 < 2*num_rows - 1):
                    maze[2*i+1,2*j] = MAP_WALL
                if (2*j + 1 < 2*num_cols - 1) and (2*i + 1 < 2*num_rows - 1):
                    maze[2*i+1,2*j+1] = MAP_WALL
        
        return maze

    def make(self,shape,startposition):
        if self.method == 'backtracker':
            M = self.__backtracker(shape,startposition)
        if self.method == 'Prim':
            M = self.__prim(shape,startposition)
        if self.method == 'division':
            M = self.__division(shape,startposition)


        return self.__transform(M=M,shape=shape,startposition=startposition)