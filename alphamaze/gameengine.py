import numpy as np 
import mazegenerator
import player

class GameEngine:
    def __init__(self,shape,player):
        self.shape = shape # (Nx,Ny)

        self.maze = None
        self.point = None
    
        self.targetposition = None
        self.pointposition = None
        self.iswin = False

        self.player = player

    def getmaze(self):
        return self.maze

    def start(self):
        mazemaker = mazegenerator.MazeMaker()
        self.maze = mazemaker.make(shape=self.shape,startposition=(0,0))

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