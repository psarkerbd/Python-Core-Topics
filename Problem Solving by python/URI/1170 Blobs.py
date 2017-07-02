
# coding: utf-8

# In[ ]:

# Author: Pranta Sarker
# URI 1170-Blobs


# In[1]:

N = input();

for i in range(N):
    capacity = input();
    #print 'capacity = ' , capacity;
    cnt = 0;
    while capacity > 1.0:
        capacity/=2.0;
        #print 'capacity = ' , capacity;
        cnt+=1;
    print cnt, 'dias';

