import ui
import gameengine
import player

class MazeGame:
    def __init__(self,shape):
        self.shape = shape

        self.gameengine = None
        self.ui = None
        self.player = player.Human()

    def start(self):
        self.gameengine = gameengine.GameEngine(shape=self.shape,player=self.player)
        self.gameengine.start()

        maze = self.gameengine.getmaze()
        self.ui = ui.UI(pressaction=self.player.setdirection,maze=maze)
        self.ui.start()
        
        while self.gameengine.update():
            self.ui.setmaze(maze=self.gameengine.getmaze())

        self.ui.gameend()

if __name__=="__main__":
    shape = (40,40)
    retrosnake = RetroSnake(shape)
    retrosnake.start()