import sys
sys.path.append("..")

import alphamaze
import numpy as np

if __name__=='__main__':
    shape = (30,30)
    startposition = (0,0)
    mazemaker = alphamaze.MazeMaker()
    #mazemaker = alphamaze.MazeMaker(method='Prim')
    #mazemaker = alphamaze.MazeMaker(method='division')

    maze = mazemaker.make(shape=shape,startposition=startposition)

    ui = alphamaze.ui.UI(pressaction=lambda x:x,maze=maze)
    ui.start()