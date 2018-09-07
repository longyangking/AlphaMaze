import numpy as np 
import argparse

__version__ = "0.0.1"
__author__ = "Yang Long"
__info__ = "Play Maze Game with AI"

__default_board_shape__ = 30, 30
__default_state_shape__ = *__default_board_shape__, 1

if __name__=='__main__':

    parser = argparse.ArgumentParser(description=__info__)

    parser.add_argument("--retrain", action='store_true', default=False, help="Re-Train AI")
    parser.add_argument("--train",  action='store_true', default=False, help="Train AI")
    parser.add_argument("--verbose", action='store_true', default=False, help="Verbose")
    parser.add_argument("--playbyai", action='store_true', default=False, help="Play by AI")
    parser.add_argument("--play", action='store_true', default=False, help="Play by human")

    args = parser.parse_args()
    verbose = args.verbose

    if args.train:
        print("Train AI")

    if args.retrain:
        print("Re-train AI")

    if args.playbyai:
        print("Play with AI!")

    if args.play:
        print("Play Maze game. Please close game in terminal after closing window (i.e, Press Ctrl+C).")
        from mazegame import MazeGame

        mazegame = MazeGame(shape=__default_board_shape__)
        mazegame.start()