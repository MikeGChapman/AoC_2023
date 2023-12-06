# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: chapmamg
"""
import numpy as np
filename = "inputs.txt"

times = [45,97,72,95]
dists = [305,1062,1110,1695]

i=0
record = np.zeros(np.shape(dists))
for time in times:
    for hold_time in range(0,time+1):
        test_dist = (time-hold_time)*hold_time
        if test_dist > dists[i]:
            record[i] = record[i]+1
    i=i+1

value_1 = record[0]*record[1]*record[2]*record[3]
print(int(value_1))
    
