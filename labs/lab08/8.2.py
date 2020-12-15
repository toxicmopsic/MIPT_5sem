#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ConsoleIterator:
    def __iter__(self):
        self.numbers = []
        return self

    def __next__(self):
        flag = True
        while flag:
            if flag and len(self.numbers) == 0:
                str = input().split()
                for i in str:
                    if i.isdigit():
                        self.numbers.append(int(i))
                    else:
                        flag = False
            elif len(self.numbers) != 0:
                return self.numbers.pop(0)
        raise StopIteration


total_sum = 0

for number in ConsoleIterator():
    total_sum = total_sum + number

print(f'Sum of entered numbers is {total_sum}')

