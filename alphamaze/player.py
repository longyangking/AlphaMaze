import numpy as np 

class Computer:
    def __init__(self):
        pass

    def play(self,maze):
        pass


class Human:
    def __init__(self):
        self.direction = (0,0)
        self.activate = False

    def setdirection(self,mode)
        if mode == 0:
            self.direction = (1,0)
        elif mode == 1:
            self.direction = (-1,0)
        elif mode == 2:
            self.direction = (0,1)
        elif mode == 3:
            self.direction = (0,-1)
        
        self.activate = True

    def play(self,maze):
        if self.activate:
            self.activate = False
            return direction
        return (0,0)