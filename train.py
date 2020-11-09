from environment import environment
import wandb

def train():
    e = environment()
    e.start()
    e.save() 


wandb.agent('hakanonal/tic-tac-toe/bcb86vib',function=train)
