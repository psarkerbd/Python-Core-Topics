
# coding: utf-8

# In[1]:

# Author: Pranta Sarker
# Aula Baula batash 


# In[2]:

# Main code goes from here....


# In[ ]:

from __future__ import print_function

def sol(string):
    strlen = len(string);
    x = int(string[0]);
    y = int(string[strlen-1]);
    if(x == y):
        ans = x * y;
    else:
        if(string[1]>='A' and string[1]<='Z'):
            ans = y - x;
        else:
            ans = x + y;
    return ans;

tc = input();

for test in range(tc):
    inp = raw_input();
    res = sol(inp);
    print(res , end='\n');

