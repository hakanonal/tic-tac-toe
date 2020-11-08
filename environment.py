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
        self.agent = agent(
            discount=self.config['discount'],
            exploration_rate=self.config['exploration_rate'],
            decay_factor=self.config['decay_factor'],
            learning_rate=self.config['learning_rate']
            )
        self.initGame()
        self.metrics = {
            #'tot_win' : 0,
            #'tot_draw' : 0,
            #'tot_lose': 0,
            #'exploration_rate' : self.agent.exploration_rate,
        }

    def initGame(self):
        #self.state = {'player_sum':0,'dealer_sum':0} 

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

    def play(self,action):
        new_state = self.state.copy()
        ended = False
#        if action:
#            new_state['player_sum'] += self.hit()
#        else:
#            ended = True
#        if new_state['player_sum'] > 21:
#            ended = True
        return new_state, ended
                
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