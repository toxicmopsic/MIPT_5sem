#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import randrange


numbers = [randrange(-40, 40) for i in range(40)]
g1 = (x for x in numbers if x > 0)
result_numbers1 = (x**2 for x in g1)
result_numbers2 = (x % 3 for x in result_numbers1)

result = [i for i in result_numbers2]

print(result)


# In[ ]:




