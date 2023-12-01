# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:46:18 2023

@author: chapmamg
"""

filename = "inputs.txt"

with open(filename) as f:
    lines = f.readlines()
    print (lines)
  
total_num = 0
for line in lines:
    breaker = 0
    
    for i in range(0,len(line)):
        if breaker == 0:
            if line[i].isdigit():
                first_num = line[i]
                breaker = 1
                
    breaker = 0
    for i in reversed(range(0,len(line))):
        if breaker == 0:
            if line[i].isdigit():
                last_num = line[i]
                breaker = 1        
                
    num = int(first_num+last_num)
    total_num = total_num +num
print(total_num)