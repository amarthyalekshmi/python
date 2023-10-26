#!/usr/bin/env python
# coding: utf-8

# In[4]:


list1=[]
for i in range(0,5):
    n=int(input("enter the integers:"))
    list1.append(n)
print(list1)
list1=[i for i in list1 if i>0]
print("positive numbers of the list:",list1)


# 
