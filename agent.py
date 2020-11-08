import numpy as np
import random
import pickle
import wandb

class agent:

    def __init__(self,discount,exploration_rate,decay_factor, learning_rate):
        self.discount = discount # How much we appreciate future reward over current
        self.exploration_rate = exploration_rate # Initial exploration rate
        self.decay_factor = decay_factor
        self.learning_rate = learning_rate
        self.q_table = {}
        
    def get_next_action(self, state):
        if random.random() < self.exploration_rate: # Explore (gamble) or exploit (greedy)
            return self.random_action()
        else:
            return self.greedy_action(state)

    def greedy_action(self, state):
        return np.argmax(self.getQ(state))
    def random_action(self):
        return random.random() > 0.5

    def getQ(self,state):
        player_sum = state['player_sum']
        dealer_sum = state['dealer_sum']
        if (player_sum,dealer_sum) not in self.q_table:
            self.q_table[(player_sum,dealer_sum)] = [0,0]
        return self.q_table[(player_sum,dealer_sum)]

    def train(self, old_state, new_state, action, reward):
        
        old_state_prediction = self.getQ(old_state)[action]
        new_state_prediction = self.getQ(new_state)

        old_state_prediction = ((1-self.learning_rate) * old_state_prediction) + (self.learning_rate * (reward + self.discount * np.amax(new_state_prediction)))

        #self.q_table[(old_state['player_sum'],old_state['dealer_sum'])][action] = old_state_prediction
        return old_state_prediction

    def update(self, old_state, new_state, action, reward):        
        reward = self.train(old_state, new_state, action, reward)
        self.exploration_rate *= self.decay_factor
        return reward

    def save(self, file="policy"):
        fw = open(file, 'wb')
        pickle.dump(self.q_table, fw)
        fw.close()
        wandb.save(file)

    def load(self, file="policy"):
        fr = open(file, 'rb')
        self.q_table = pickle.load(fr)
        fr.close()        