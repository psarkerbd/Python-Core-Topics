
# coding: utf-8

# In[1]:

# Author: Pranta Sarker


# In[2]:

while True:
    n = input();
    if(n==0):
        break;
    ans = n * (n + 1) * ((2 * n) + 1);
    ans/=6;
    print ans;

