# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: chapmamg
"""
import numpy as np
filename = "inputs.txt"

with open(filename) as f:
    lines = f.readlines()
    # print (lines)
  
total_num = 0
i=0
j=0
max_val = 0
# find the highest value
for line in lines:
    # print(line)
    
    if i == 0:
        seed_values_str = line.split(": ")[1].split("\n")[0].split(" ")
        seed_values = np.array(seed_values_str).astype(int)
        print(seed_values)
    else:
        if line == "\n":
            line = line
        elif line[0].isalpha():
            line = line
        elif line[0].isnumeric():
            max_val_local = max([int(line.split(" ")[0]),int(line.split(" ")[1])])+int(line.split(" ")[2])
            print(max_val_local)
            if max_val_local > max_val:
                max_val = max_val_local
                print(max_val)
    i=i+1
    
    
# for line in lines:
#         # print(line)
        
#         if i == 0:
#             seed_values_str = line.split(": ")[1].split("\n")[0].split(" ")
#             seed_values = np.array(seed_values_str).astype(int)
#             print(seed_values)
#         else:
#             if line == "\n":
#                 line = line
#             elif line[0].isalpha():
                
#             elif line[0].isnumeric():
#     try:
#         breaker = 0
#         print(line)
#         card_id = line.split(": ")[0]
#         print("card_id = " + card_id)
#         winning_nums_str = line.split(": ")[1].split("|")[0]
#         winning_nums = np.array(winning_nums_str.split(" "))
#         clipped_winning_nums = np.array([i for i in winning_nums if i])
#         print("winning_nums_str = " + winning_nums_str)
#         try:
#             my_nums_str = line.split(": ")[1].split("|")[1].split("}")[0]
#         except:
#             my_nums_str_old = line.split(": ")[1].split("|")[1].split("\\n")[0]
#             my_nums_str = my_nums_str_old[0,len(my_nums_str_old)-1]
#         my_nums = np.array(my_nums_str.split(" "))
#         clipped_my_nums = np.array([i for i in my_nums if i])
        
        
#         print("my_nums_str = " + my_nums_str)
        
#         num_matches = 0
#         for i in range(0,len(clipped_my_nums)):
#             if clipped_my_nums[i] in clipped_winning_nums:
#                 if num_matches == 0:
#                     num_matches = num_matches +1
#                 else: 
#                     num_matches=num_matches*2
#         print (num_matches)
#         total_num = total_num+num_matches
#     except:
#         j=j+1
#         print(line)

# print("total_num = " + str(total_num))
# print("j = " + str(j))