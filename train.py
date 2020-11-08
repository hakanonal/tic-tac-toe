from environment import environment
import wandb

def train():
    e = environment()
    e.start()
    e.agent.save()
    e.agent.printQTable()    


wandb.agent('hakanonal/tic-tac-toe/xxxx',function=train)
