#!/usr/bin/env python
# coding: utf-8

# In[7]:


list1=[]
square=[]
for i in range(0,5):
    n=int(input("enter the numbers:"))
    list1.append(n)
print(list1)
square=[i*i for i in list1]
print("the square of the given numbers:",square)


# 
