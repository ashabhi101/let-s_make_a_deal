#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


trials=int(input('Enter number of trials to run:'))
switch = int(input('Enter 0 for no switching and 1 if you want to switch:'))


# In[3]:


doors = ["A", "B", "C"]
np.random.seed(0)
# the prize is in this door
prize = []
for i in range(trials):
    prize.append(np.random.choice(doors))


# In[4]:


## Now you are picking a door, choices are saved to userchoice


# In[5]:


'''userchoice = []
for i in range(0,trials):
    userchoice.append(np.random.choice(doors))'''


# In[6]:


userchoice = ["A"]*trials


# In[7]:


revealed, unrevealed= [], []
for i in range(trials):
    a= prize[i]
    b =userchoice[i]
    temp=[]
    if prize[i] == userchoice[i]:
        temp = list(set(doors)-set(a))
        revealed.append(temp[1])
        unrevealed.append(temp[0])
    else:
        temp = list(set(doors)-set(a)-set(b))
        revealed.append(temp[0])
        unrevealed.append(prize[i])   


# In[8]:


win, lose = 0,0
for i in range(trials):
    if switch == 0:
        if prize[i] == userchoice[i]:
            win+=1
        else:
            lose+=1
    if switch ==1:
        if prize[i] == userchoice[i]:
            lose+=1
        else:
            win+=1

if switch:
    print("You win", win,"times and you made a good choice in terms of probability")
else:
    print("You win", win, "times and you made a bad choice in terms of probability")

