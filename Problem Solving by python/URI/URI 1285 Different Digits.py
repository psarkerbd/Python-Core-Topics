
# coding: utf-8

# In[ ]:

# Author: Pranta Sarker
# URI 1285


# In[ ]:

# Testing..

def Isrepeating(string):
    for i in range(0 , 10):
        cnt = string.count(str(i));
        if(cnt > 1):
            return False;
    return True;

N = input();
M = input();

count = 0;

for i in range(N , M+1):
    res = Isrepeating(str(i));
    if(res == True):
        count+=1;
print count;


# In[ ]:

# Main Code goes to.....

from __future__ import print_function;

def Isrepeating(string):
    for i in range(len(string)): # size of the number
        cnt = string.count(string[i]);
        if(cnt > 1):
            return False;
    return True;

while True:
    try:
        a , b = raw_input().split(' ');
        x = int(a);
        y = int(b);
        cnt = 0;
        for i in range(x , y+1):
            res = Isrepeating(str(i));
            if(res == True):
                cnt+=1;
        print(cnt , end='\n');
    except EOFError:
        break;

