# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:46:18 2023

@author: chapmamg
"""
import numpy as np

filename = "inputs.txt"

with open(filename) as f:
    lines = f.readlines()
#    print (lines)
total_1 = 0
game_number = np.zeros(len(lines),dtype=int)
red = np.zeros([len(lines),25],dtype=int)
green = np.zeros([len(lines),25],dtype=int)
blue = np.zeros([len(lines),25],dtype=int)
i=0


for line in lines:
    breaker = 0
    game_number[i]=int(line.split("Game ")[1].split(":")[0])
    
    line_cut = line.split(": ")[1].split("\n")[0]
#    print(line_cut)
    round_split = line_cut.split("; ")
#    print(round_split)
    for j in range(0,len(round_split)):
        color_split = round_split[j].split(", ")
        for k in range(0,len(color_split)):
            if "red" in color_split[k]:
#                print(color_split[k])
                red[i,j]=int(color_split[k].split(" ")[0])
            if "green" in color_split[k]:
#                print(color_split[k])
                green[i,j]=int(color_split[k].split(" ")[0])
            if "blue" in color_split[k]:
#                print(color_split[k])
                blue[i,j]=int(color_split[k].split(" ")[0])
    
    
    
    
    if max(red[i,:])<13:
        if max(green[i,:])<14:
            if max(blue[i,:])<15:
                total_1 = total_1+game_number[i]
    i=i+1          
print(total_1)