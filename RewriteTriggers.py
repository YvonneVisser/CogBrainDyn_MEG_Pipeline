# Rewriting events from timelimit experiment, this is input:

# STI015 = button press
# STI001 = DEC 1 = clock appears
# STI002 = DEC 2 = 2 second condition starts
# STI003 = DEC 4 = 4 second condition starts
# STI004 = DEC 8 = 8 second condition starts
# STI005 = DEC 16 = 16 second condition starts
# STI006 = DEC 32 = infinite condition starts
# STI007 = DEC 64
# STI008 = DEC 128 = break

# rewrite so that single "trigger channel" has different event values for button presses in each condition
# This will allow you to epoch to those events, and seperate conditions too

"""
Created on Mon Feb 11 16:20:40 2019

@author: Yvonne F. Visser
"""

import mne
import numpy as np


from mne.parallel import parallel_func

def RewriteTriggers(raw):

    # find triggers
    Cond2 = mne.find_events(raw, output = 'onset', shortest_event = 1, stim_channel = 'STI002')
    Cond4 = mne.find_events(raw, output = 'onset', shortest_event = 1, stim_channel = 'STI003')
    Cond8 = mne.find_events(raw, output = 'onset', shortest_event = 1, stim_channel = 'STI004')
    Cond16 = mne.find_events(raw, output = 'onset', shortest_event = 1, stim_channel = 'STI005')
    CondInf = mne.find_events(raw, output = 'onset', shortest_event = 1, stim_channel = 'STI006')
    
    # combine all trigger samples together
    w = 20
    h = 5
    Cond = [[0 for x in range(w)] for y in range(h)] 
    
    Cond[0] = Cond2[:,0]
    Cond[1] = Cond4[:,0]
    Cond[2] = Cond8[:,0]
    Cond[3] = Cond16[:,0]
    Cond[4] = CondInf[:,0]
            
    BP = mne.find_events(raw, output = 'onset', shortest_event = 1, stim_channel = 'STI015')
        

    # For each move, find closest condition trigger

    condition = np.zeros((len(BP[:,0]),1))
    for i,move in enumerate(BP[:,0]): # for each button press in data
        Diff = (move-Cond) # find difference in samples between each condition and this move
        pos_Diff = Diff 
        for row in range(0,5): # select only positive values (condition happened before move)
            pos_Diff[row]=[x for x in Diff[row] if not (x<0)]
        Min = min([min(element, default=10000000) for element in pos_Diff]) # find the smallest difference (empty becomes 10000000)
        for row in range(0,5):
            if np.isin(Min, pos_Diff[row]): # if this row has the minimum
                condition[i] = row # assign the row as this conditon (limit)
                
    
    # save new trigger values in way MNE understands
    
    w = 3
    h = len(BP[:,0])
    events = np.zeros((h,w))
    first_event = np.zeros((1,3))
    
    # add first sample number to events array so that mne.epochs doesn`t break
    first_event[0,0] = raw.first_samp
    first_event[0,1] = 0
    first_event[0,2] = 1
    
    # define each event with 1) sample number, 2) value before and 3) value after
    for i,event in enumerate(events):
        events[i,0] = BP[i,0] # column 1 has sample number of move
        events[i,1] = 0 # column 2 has event value before (0)
        
        # column 3 has different value for each conditon (see below)
        if condition[i] == 0:
            events[i,2] = 2
        elif condition [i] == 1:
            events[i,2] = 4
        elif condition [i] == 2:
            events[i,2] = 8
        elif condition [i] == 3:
            events[i,2] = 16
        elif condition [i] == 4:
            events[i,2] = 32
            
    # add first sample and other events together
    events = np.concatenate([first_event, events], axis = 0)
                
        
    """ 
    Now events variable has 3 columns, 1 is the time (in samples?) of the button press event
    column 2 has all zeros (the trigger value "before") and column 3 has the following values:
    2 if button press was in 2 second condition
    4 if button press was in 4 second condition
    8 if button press was in 8 second conditon
    16 if button press was in 16 second condition
    32 if button press was in infinite condition
    """
                                                                            
    return events
