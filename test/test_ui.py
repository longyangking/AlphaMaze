import sys
sys.path.append("..")

import alphamaze
import numpy as np

maze = np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,-1,0,-1,-1,-1,0,-1,0],
    [0,-1,-1,0,-1,-1,-1,0,-1,0],
    [0,-1,-1,-1,-1,0,0,-1,-1,0],
    [0,-1,0,0,0,-1,-1,-1,-1,0],
    [0,-1,-1,-1,0,-1,-1,-1,-1,0],
    [0,-1,0,-1,-1,-1,0,-1,-1,0],
    [0,-1,0,0,0,-1,0,0,-1,0],
    [0,0,-1,-1,-1,-1,-1,-1,2,0],
    [0,0,0,0,0,0,0,0,0,0]
])
ui = alphamaze.ui.UI(pressaction=lambda x:x,maze=maze)
ui.start()