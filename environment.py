import random
from agent import agent
import wandb

class environment:

    def __init__(self, config=None):

        if(config is None):
            wandb.init(project="tic-tac-toe")
            self.config = wandb.config
        else:
            wandb.init(project="tic-tac-toe",config=config)
            self.config = config
        self.agentX = agent(
            discount=self.config['discount'],
            exploration_rate=self.config['exploration_rate'],
            decay_factor=self.config['decay_factor'],
            learning_rate=self.config['learning_rate'],
            'X'
            )
        self.agentO = agent(
            discount=self.config['discount'],
            exploration_rate=self.config['exploration_rate'],
            decay_factor=self.config['decay_factor'],
            learning_rate=self.config['learning_rate'],
            'O'
            )
        self.initGame()
        self.metrics = {
            'x_win' : 0,
            'o_win' : 0,
            'tie': 0,
            'exploration_rate' : self.agent.exploration_rate,
        }

    def initGame(self):
        self.state = '         '

    def start(self):
        for episode in range(1,self.config['episode']+1):
            self.initGame()
            #player turn
            while True:
                action_to_play = self.agent.get_next_action(self.state)
                new_state, ended = self.play(action_to_play)
                self.actions_played.append((self.state,new_state,action_to_play))
                self.state = new_state
                if ended:
                    break

            self.metrics['exploration_rate'] = self.agent.exploration_rate
            wandb.log(self.metrics,step=episode)

                
    def findWinner(self):
#        # player 1 | draw 0 | dealer -1
#        winner = 0
#        if self.state['player_sum'] > 21:
#            if self.state['dealer_sum'] > 21:
#                winner = -1
#            else:
#                winner = -1
#        else:
#            if self.state['dealer_sum'] > 21:
#                winner = 1
#            else:
#                if self.state['player_sum'] < self.state['dealer_sum']:
#                    winner = -1
#                elif self.state['player_sum'] > self.state['dealer_sum']:
#                    winner = 1
#                else:
#                    winner = 0
#        return winner
    
#    def debug1(self,episode,old_state,new_state,action):
#        if(self.config['debug']):
#            print("%d = %s -> %s -> %s"%(episode,old_state,action,new_state))
#            input("continue?")