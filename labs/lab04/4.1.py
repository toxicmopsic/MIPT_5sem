#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def author(author):
    def wrapper(func):
        func._author = author  
        return func
    return wrapper

@author("Captain Friedrich Von Schoenvorts")
def add2(num: int) -> int:
    return num + 2

print(add2._author)

