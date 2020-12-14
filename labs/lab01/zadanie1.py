#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers_list = list(map(float, str(input()).split(' ')))
numbers_list


# In[2]:


print([num**2 for num in numbers_list])


# In[3]:


numbers_list = list(map(lambda x: float(x)**2, str(input()).split(' ')))
numbers_list


# In[4]:


def squarer():
    return list(map(lambda x: int(x)**2, str(input()).split(' ')))


# In[5]:


def printer(x):
    x = sorted(list(set(x)))


# In[6]:


class Squarer():
    def __init__(self):
        self.__squares_list = []
        self.__squarer()
        
    def __squarer(self):
        self.__squares_list = list(map(lambda x: float(x)**2, str(input()).split(' ')))
    
    def __repr__(self):
        return ' '.join(map(str, sorted(list(set(self.__squares_list)))))


# In[7]:


Squarer()


# In[ ]:




