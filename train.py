from environment import environment
import wandb

def train():
    e = environment()
    e.start()
    e.save() 


wandb.agent('hakanonal/tic-tac-toe/xxxx',function=train)
