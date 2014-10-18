import numpy as np
from itertools import cycle

def light_state(t, t_0, t_green, t_red):
    """Return the state of the light at t given that the light went green at t_0."""
    states = ['red', 'green']
    t_cycle = t_green + t_red
    if t % t_cycle < t_green:
        state_index = 1
        time_left = t_green - (t % t_cycle)
    else:
    	state_index = 0
    	time_left = t_cycle - (t % t_cycle)
    return '{0}, goes {1} in {2} seconds!'.format(
    	states[state_index], 
        states[(state_index + 1) % 2],
        time_left)

