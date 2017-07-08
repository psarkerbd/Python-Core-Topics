
# coding: utf-8

# In[ ]:

# Author: Pranta Sarker


# In[3]:

from __future__ import print_function;

while True:
    T , N = raw_input().split(' ');
    test = int(T);
    match = int(N);
    if(test==0 and match==0):
        break;
    
    cnt = 0;
    points = 0;
    
    for tc in range(test):
        detail = raw_input().split(' ');
        tmp = int(detail[1]);
        points += tmp;
    winingpoints = 3 * match;
    cnt = winingpoints - points;
    print(cnt , end='\n');

