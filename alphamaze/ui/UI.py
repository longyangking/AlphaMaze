import numpy as np 
import threading
from . import nativeUI

import sys
from . import config
from PyQt5.QtWidgets import QApplication

class UI(threading.Thread):
    def __init__(self,pressaction,maze):
        threading.Thread.__init__(self)
        self.ui = None
        self.app = None

        self.maze = maze
        self.sizeunit = config.sizeunit
        self.pressaction = pressaction
    
    def run(self):
        print('Init UI...')
        self.app = QApplication(sys.argv)
        self.ui = nativeUI.nativeUI(pressaction=self.pressaction,maze=self.maze,sizeunit=self.sizeunit)
        self.app.exec_()

    def setmaze(self,maze):
        while not self.ui:
            pass
            
        return self.ui.setmaze(maze)
    
    def gameend(self):
        while not self.ui:
            pass
            
        self.ui.gameend()