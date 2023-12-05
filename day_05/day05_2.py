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

max_val = 0
var_type = ["seed","soil","fertilizer","water","light","temperature","humidity","location",]
j=-1

for line in lines:
    # print(line)
    
    if i == 0:
        seed_values_str = line.split(": ")[1].split("\n")[0].split(" ")
#        print(seed_values_str)
        seed_values_int = np.array(seed_values_str).astype(dtype=np.int64)
        seed_values = np.array([seed_values_int[i]])
        for i in range(0,np.shape(seed_values_int)[0],2):
            new_array = np.array(range(seed_values_int[i],seed_values_int[i]+seed_values_int[i+1],10000)).astype(dtype=np.int64)
            seed_values = np.concatenate((seed_values,new_array))
#        print(seed_values)
        ref_tracker = np.zeros([np.shape(var_type)[0],np.shape(seed_values)[0]])
        ref_tracker[0,:]=seed_values
    else:
        if line == "\n":
            for k in range(0,np.shape(seed_values)[0]):
                if ref_tracker[j+1,k] == 0:
                    ref_tracker[j+1,k]=ref_tracker[j,k]
        elif line[0].isalpha():
            j=j+1
        elif line[0].isnumeric():
            for k in range(0,np.shape(seed_values)[0]):
               # check if value is in range
               if ref_tracker[j,k] > int(line.split(" ")[1])-1:
                   if ref_tracker[j,k] < int(line.split(" ")[1])+int(line.split(" ")[2])+1:
                       ref_tracker[j+1,k]=int(line.split(" ")[0])-int(line.split(" ")[1])+ref_tracker[j,k]

    i=i+1
    

    
for k in range(0,np.shape(seed_values)[0]):
    if ref_tracker[j+1,k] == 0:
        ref_tracker[j+1,k]=ref_tracker[j,k]
    
value_1 = int(min(ref_tracker[np.shape(var_type)[0]-1,:]))
print(value_1)


seed_index = ref_tracker[0,np.where(ref_tracker[np.shape(var_type)[0]-1,:] == value_1)]
seed_index = int(seed_index[0,0])
print(seed_index)

total_num = 0
i=0

max_val = 0
var_type = ["seed","soil","fertilizer","water","light","temperature","humidity","location",]
j=-1

for line in lines:
    # print(line)
    
    if i == 0:
        seed_values_str = line.split(": ")[1].split("\n")[0].split(" ")
#        print(seed_values_str)
        seed_values_int = np.array(seed_values_str).astype(dtype=np.int64)
        seed_values = np.array(range(seed_index-10000,seed_index+10000))
        
        ref_tracker = np.zeros([np.shape(var_type)[0],np.shape(seed_values)[0]])
        ref_tracker[0,:]=seed_values
    else:
        if line == "\n":
            for k in range(0,np.shape(seed_values)[0]):
                if ref_tracker[j+1,k] == 0:
                    ref_tracker[j+1,k]=ref_tracker[j,k]
        elif line[0].isalpha():
            j=j+1
        elif line[0].isnumeric():
            for k in range(0,np.shape(seed_values)[0]):
               # check if value is in range
               if ref_tracker[j,k] > int(line.split(" ")[1])-1:
                   if ref_tracker[j,k] < int(line.split(" ")[1])+int(line.split(" ")[2]):
                       ref_tracker[j+1,k]=int(line.split(" ")[0])-int(line.split(" ")[1])+ref_tracker[j,k]

    i=i+1
    
for k in range(0,np.shape(seed_values)[0]):
    if ref_tracker[j+1,k] == 0:
        ref_tracker[j+1,k]=ref_tracker[j,k]
    
value_2 = min(ref_tracker[np.shape(var_type)[0]-1,:])
print(value_2)




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

