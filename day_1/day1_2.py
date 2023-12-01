# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:46:18 2023

@author: chapmamg
"""

filename = "inputs.txt"

with open(filename) as f:
    lines = f.readlines()

  
number_words_3 = ['one',
                'two',
                'six',]

number_words_3_num = ["1","2","6"]

number_words_4 = ['four',
                'five',
                'nine']

number_words_4_num = ["4","5","9"]

number_words_5 = ['three',
                'seven',
                'eight',]

number_words_5_num = ["3","7","8"]

total_num = 0
for line in lines:
#    print(line)
#    for i in range(0,len(number_words)):
#        line = line.replace(number_words[i],str(i+1))
#    print(line)
    
    
    breaker = 0
    
    for i in range(0,len(line)):
        if breaker == 0:
            
            for j in range(0,len(number_words_3)):
                if line[i:i+3] == number_words_3[j]:
                    first_num = number_words_3_num[j]
                    breaker = 1
            for j in range(0,len(number_words_4)):        
                if line[i:i+4] == number_words_4[j]:
                    first_num = number_words_4_num[j]
                    breaker = 1
            for j in range(0,len(number_words_5)):
                if line[i:i+5] == number_words_5[j]:
                    first_num = number_words_5_num[j]
                    breaker = 1
                    
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
        if breaker == 0:
            
            for j in range(0,len(number_words_3)):
                if line[i-3:i] == number_words_3[j]:
                    last_num = number_words_3_num[j]
                    breaker = 1
            for j in range(0,len(number_words_4)):        
                if line[i-4:i] == number_words_4[j]:
                    last_num = number_words_4_num[j]
                    breaker = 1
            for j in range(0,len(number_words_5)):
                if line[i-5:i] == number_words_5[j]:
                    last_num = number_words_5_num[j]
                    breaker = 1
                    

                
    num = int(first_num+last_num)
    total_num = total_num +num
print(total_num)