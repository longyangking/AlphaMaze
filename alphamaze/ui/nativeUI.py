import numpy as np 
import sys

from PyQt5.QtWidgets import QWidget, QApplication,QDesktopWidget
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

class nativeUI(QWidget):
    playsignal = pyqtSignal(int) 

    def __init__(self,pressaction,maze,sizeunit):
        super(nativeUI,self).__init__(None)
        self.maze = maze
        self.sizeunit = sizeunit

        self.ax = sizeunit
        self.ay = sizeunit

        self.isgameend = False
        self.pressaction = pressaction

        self.playsignal.connect(self.pressaction) 
        self.initUI()

    def setmaze(self,maze):
        self.maze = maze
        self.update()

    def initUI(self):
        (Nx,Ny) = self.maze.shape
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()

        self.setGeometry((screen.width()-size.width())/2, 
                        (screen.height()-size.height())/2,
                        Nx*self.sizeunit, Ny*self.sizeunit)
        self.setWindowTitle("Maze")

        # set Background color
        palette =  QPalette()
        palette.setColor(self.backgroundRole(), QColor(255,255,255))
        self.setPalette(palette)

        #self.setMouseTracking(True)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        self.drawmaze(qp)

        if self.isgameend:
            self.drawgameend(qp)

        qp.end()

    def gameend(self):
        self.isgameend = True

    def drawgameend(self,qp):
        size =  self.geometry()
        qp.setPen(0)
        qp.setBrush(QColor(200, 200, 200, 180))
        width = size.width()/5*4
        height = size.height()/3
        qp.drawRect(size.width()/2-width/2, size.height()/2-height/2, width, height)

        qp.setPen(QColor(0,0,0))
        font = qp.font()
        font.setPixelSize(width/5)
        qp.setFont(font)
        qp.drawText(QRect(size.width()/2-width/2, size.height()/2-height/2, width, height),	0x0004|0x0080,str("Game End")) 
    
    def resizeEvent(self,e):
        (Nx,Ny) = self.maze.shape
        size =  self.geometry()
        width = size.width()
        height = size.height()
        self.ax = width/Nx
        self.ay = height/Ny
    
    def keyPressEvent(self,e):
        mode = -1
        if e.key() == Qt.Key_Up:
            mode = 3
        elif e.key() == Qt.Key_Down:
            mode = 2
        elif e.key() == Qt.Key_Left:
            mode = 1
        elif e.key() == Qt.Key_Right:
            mode = 0
            
        if mode != -1:
            self.playsignal.emit(mode)

    def drawmaze(self, qp):
        (Nx,Ny) = self.maze.shape
        qp.setPen(Qt.NoPen)
        for i in range(Nx):
            for j in range(Ny):
                if self.maze[i,j] == 1:
                    qp.setBrush(QColor(255, 0, 0))  # Player
                elif self.maze[i,j] == 0:
                    qp.setBrush(QColor(255, 255, 255))  # Ground
                elif self.maze[i,j] == 2:
                    qp.setBrush(QColor(255,255,0)) # Target
                elif self.maze[i,j] == -1:
                    qp.setBrush(QColor(0,0,0)) # Wall
                qp.drawRect(i*self.ax, j*self.ay ,self.ax,self.ay)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    maze = np.random.randint(-1,3,size=(30,30))
    sizeunit = 20
    ex = nativeUI(pressaction=lambda x:x,maze=maze,sizeunit=sizeunit)
    sys.exit(app.exec_())

