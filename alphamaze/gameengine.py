import numpy as np 
import mazegenerator
import point

class GameEngine:
    def __init__(self,shape,player):
        self.shape = shape # (Nx,Ny)

        self.maze = None
        self.point = None
    
        self.targetposition = None
        self.pointposition = None
        self.iswin = False

        self.player = player

    def __findallvalidplaces(self):
        (Nx,Ny) = self.shape
        places = list(range(Nx*Ny))
        for i in range(Nx):
            for j in range(Ny):
                place = j*Nx + i 
                pos = self.__place2pos(place)
                if self.maze[pos] != 0:
                    places.remove(place)

        return places

    def __place2pos(self,place):
        (Nx,Ny) = self.shape
        pos = (int(place/Nx),place%Nx)
        return pos

    def getmaze(self):
        return self.maze

    def start(self):
        mazemaker = mazegenerator.MazeMaker()
        self.maze = mazemaker.make(shape=self.shape,startposition=(0,0))
        self.shape = self.maze.shape

        # Target Position
        validplaces = self.__findallvalidplaces()
        choice = np.random.randint(len(validplaces))
        position = self.__place2pos(validplaces[choice])
        self.targetposition = position
        self.maze[position] = 2

        # Point Position
        self.point = point.Point(position=(0,0),player=self.player)
        self.pointposition = self.point.getposition()
        self.maze[self.pointposition] = 1

    def refreshmaze(self):
        position = self.point.getposition()
        self.maze[self.pointposition] = 0
        self.maze[position] = 1
        self.pointposition = position

    def update(self):
        self.point.update(self.maze)
        self.refreshmaze()

        return self.point.iswin()