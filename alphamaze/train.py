import numpy as np 
from ai import AI 

class SelfplayEngine:
    def __init__(self, ai, verbose):
        self.ai = ai

        self.state_shape = ai.get_state_shape()
        self.verbose = verbose

        self.boards = list()
        self.states = list()

    def get_state(self):
        return self.states[-1]
        
    def update_states(self):
        pass

    def start(self):


class TrainAI:
    def __init__(self, state_shape, action_dim, ai=None, verbose=False):
        self.state_shape = state_shape
        self.action_dim = action_dim
        
        if ai is not None:
            self.ai = ai
        else:
            self.ai = AI(
                state_shape=state_shape,
                action_dim=action_dim,
                verbose=verbose
            )
        
        self.losses = list()

    def get_losses(self):

    def get_selfplay_data(self, n_round):

    def update_ai(self, dataset):

    def start(self, filename):
