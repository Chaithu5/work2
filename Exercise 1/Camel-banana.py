#!/usr/bin/env python
# coding: utf-8

# In[1]:


total = int(input('How many bananas does the person have: '))
distance = int(input('What is the distance needed to cover: '))
max_capacity = int(input('What is the maximum capacity of your camel: '))

loss = 0
start = total

for i in range(distance):
    while start > 0:
        start = start - max_capacity
        if start == 1:
            loss = loss - 1
        loss = loss + 2
    loss = loss - 1
    start = total - loss
    
    if start == 0:
        break
        
print("\n", start)


# In[ ]:




