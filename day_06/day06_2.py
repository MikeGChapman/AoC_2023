# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: chapmamg
"""
import numpy as np
filename = "inputs.txt"

times = [45977295]
dists = [305106211101695]

i=0
record = np.zeros(np.shape(dists))
for time in times:
    for hold_time in range(0,time+1):
        test_dist = (time-hold_time)*hold_time
        if test_dist > dists[i]:
            record[i] = record[i]+1
    i=i+1

value_2 = record[0]
print(int(value_2))
    
