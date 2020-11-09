from environment import environment
import os

config = {
    'discount': 0.95,
    'exploration_rate':0.9,
    'decay_factor':0.99,
    'learning_rate':0.01,
    'episode':1000,
    'debug' : 0,
    'print_state' : 0
}
os.environ['WANDB_MODE'] = 'dryrun'

e = environment(config=config)

e.start()
e.save() 
