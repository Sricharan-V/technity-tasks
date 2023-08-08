#Coin Flip Streaks

import random
numberOfStreaks = 0
list=[]
count=1
freq=[]
ele=[]
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    a= random.randint(0,1)
    
    if a==0:
        list.append('H')
    else:
        list.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
for i in range(len(list)-1):
    if list[i]== list[i+1]:
        count+=1
    else:
        freq.append(count)
        ele.append(list[i])
        count=1
freq.append(count)
ele.append(list[i+1])
# print(ele, freq)
numberOfStreaks= freq.count(6)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

