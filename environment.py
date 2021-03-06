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
            sign="X"
            )
        self.agentO = agent(
            discount=self.config['discount'],
            exploration_rate=self.config['exploration_rate'],
            decay_factor=self.config['decay_factor'],
            learning_rate=self.config['learning_rate'],
            sign="O"
            )
        self.initGame()
        self.metrics = {
            'X_tot_win' : 0,
            'O_tot_win' : 0,
            'tot_draw': 0,
            'x_exploration_rate' : self.agentX.exploration_rate,
            'o_exploration_rate' : self.agentO.exploration_rate,
        }

    def initGame(self):
        self.state = "         "         
        self.actions_played = []
        self.turn = 1

    def start(self):
        for episode in range(1,self.config['episode']+1):
            self.initGame()
            #game phase
            while True:
                
                if self.turn == 1:
                    action_to_play = self.agentX.get_next_action(self.state)
                    new_state = self.agentX.play(self.state,action_to_play)
                if self.turn == -1:
                    action_to_play = self.agentO.get_next_action(self.state)
                    new_state = self.agentO.play(self.state,action_to_play)

                self.debug1(episode,self.state,new_state,action_to_play)
                self.actions_played.append((self.state,new_state,action_to_play))
                self.state = new_state
                self.printState(self.state)
                self.turn *= -1
                winner = self.findWinner()
                if winner is not None:
                    break


            #q-tatble update backpropogation phase
            if winner == 1:
                self.metrics['X_tot_win'] += 1
                self.metrics['X_avg_win'] = self.metrics['X_tot_win'] / episode
                self.agentX.update(self.actions_played,1)
                self.agentO.update(self.actions_played,-1)
            if winner == 0:
                self.metrics['tot_draw'] += 1
                self.metrics['avg_draw'] = self.metrics['tot_draw'] / episode
                self.agentX.update(self.actions_played,0)
                self.agentO.update(self.actions_played,0)
            if winner == -1:
                self.metrics['O_tot_win'] += 1
                self.metrics['O_avg_win'] = self.metrics['O_tot_win'] / episode
                self.agentX.update(self.actions_played,-1)
                self.agentO.update(self.actions_played,1)

            self.metrics['x_exploration_rate'] = self.agentX.exploration_rate
            self.metrics['o_exploration_rate'] = self.agentO.exploration_rate
            wandb.log(self.metrics,step=episode)

                
    def findWinner(self):
        # Win-X=1 | tie=0 | Win-O=-1 | game not ended=null
        if self.agentX.didIWin(self.state):
            return 1
        if self.agentO.didIWin(self.state):
            return -1
        if self.state.find(" ") == -1:
            return 0
        return None
        
    def save(self):
        self.agentX.save()
        self.agentO.save()

    
    def debug1(self,episode,old_state,new_state,action):
        if(self.config['debug']):
            print("%d = %s -> %s -> %s"%(episode,old_state,action,new_state))
            input("continue?")

    def printState(self,state):
        if(self.config['print_state']):
            print("%s|%s|%s"%(state[0],state[1],state[2]))
            print("-----")
            print("%s|%s|%s"%(state[3],state[4],state[5]))
            print("-----")
            print("%s|%s|%s"%(state[6],state[7],state[8]))
            input("continue?")
