import numpy as np 

class Point:
    def __init__(self,position,player):
        self.position = position
        self,player = player
        self.iswin = False

    def getposition(self):
        return self.position

    def iswin(self):
        return self.iswin

    def update(self,maze):
        (Nx,Ny) = maze.shape
        direction = self.player.play(maze)

        x = self.position[0] + direction[0]
        y = self.position[1] + direction[1]
        position = (x,y)

        if (0 <= x) and (x < Nx) and (0 <= y) and (y < Ny):
            if (maze[position] != -1):  # Not Wall
                self.position = position
            if (maze[position] == 2):   # Get Target
                self.iswin = True