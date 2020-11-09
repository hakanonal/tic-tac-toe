import numpy as np
import random
import pickle
import wandb

class agent:

    def __init__(self,discount,exploration_rate,decay_factor, learning_rate,sign):
        self.discount = discount # How much we appreciate future reward over current
        self.exploration_rate = exploration_rate # Initial exploration rate
        self.decay_factor = decay_factor
        self.learning_rate = learning_rate
        self.sign = sign
        self.q_table = {}
        

    def play(self,old_state,action):
        state = old_state
        assert state[action] == ' '
        state = state[:action] + self.sign + state[action+1:]
        return state

    def get_next_action(self, state):
        if random.random() < self.exploration_rate: # Explore (gamble) or exploit (greedy)
            return self.random_action(state)
        else:
            return self.greedy_action(state)

    #!!!! these action are wrong they need to give valid actions. It should be between 0 and 8 and also the action position has to be empty on the state.
    def actionSpaceOfState(self,state):
        return [pos for pos, char in enumerate(state) if char == " "]
    def greedy_action(self, state):
        action_space = self.actionSpaceOfState(state)
        filtered_q_table = []
        q_table_state = self.getQ(state)
        for i in range(9):
            if i in action_space:
                filtered_q_table.append(q_table_state[i])
            else:
                filtered_q_table.append(-999999999999)
        return np.argmax(filtered_q_table)
    def random_action(self,state):
        return random.choice(self.actionSpaceOfState(state))
    #!!!!!!!

    def getQ(self,state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(9)
        return self.q_table[state]

    def train(self, old_state, new_state, action, reward):
        
        old_state_prediction = self.getQ(old_state)[action]
        new_state_prediction = self.getQ(new_state)

        old_state_prediction = ((1-self.learning_rate) * old_state_prediction) + (self.learning_rate * (reward + self.discount * np.amax(new_state_prediction)))

        self.q_table[old_state][action] = old_state_prediction
        return old_state_prediction

    def update(self, actions_played, reward):
        for old_state,new_state,action in reversed(actions_played):
            new_reward = self.train(old_state, new_state, action, reward)
            reward = new_reward
        self.exploration_rate *= self.decay_factor

    def save(self, file="policy"):
        fw = open(file+'_'+self.sign, 'wb')
        pickle.dump(self.q_table, fw)
        fw.close()
        wandb.save(file+'_'+self.sign)

    def load(self, file="policy"):
        fr = open(file+'_'+self.sign, 'rb')
        self.q_table = pickle.load(fr)
        fr.close()  

    def didIWin(self,state):
        if state[0] == self.sign and state[1] == self.sign and state[2] == self.sign:
            return True
        if state[3] == self.sign and state[4] == self.sign and state[5] == self.sign:
            return True
        if state[6] == self.sign and state[7] == self.sign and state[8] == self.sign:
            return True
        if state[0] == self.sign and state[3] == self.sign and state[6] == self.sign:
            return True
        if state[1] == self.sign and state[4] == self.sign and state[7] == self.sign:
            return True
        if state[2] == self.sign and state[5] == self.sign and state[8] == self.sign:
            return True
        if state[0] == self.sign and state[4] == self.sign and state[8] == self.sign:
            return True
        if state[2] == self.sign and state[4] == self.sign and state[6] == self.sign:
            return True
        return False
