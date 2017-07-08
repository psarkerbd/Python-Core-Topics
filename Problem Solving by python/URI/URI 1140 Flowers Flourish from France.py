
# coding: utf-8

# In[ ]:

# Author: Pranta Sarker
# URI 1140


# In[ ]:

from __future__ import print_function

string = raw_input().split(' ');
for i in range(len(string)):
    print(string[i].lower() , end=' ');
    
print('');
print('-' * 50);


# In[ ]:

# Testing...

from __future__ import print_function

string = raw_input().split(' ');
print(string);
strlen = len(string);
tot = True;
tmp = string[0][0].lower();
for i in range(1, strlen):
    now = string[i][0].lower();
    if(tmp != now):
        tot = False;
        break;
    tmp = now;
    print(string[i][0].lower());
if(tot == False):
    print('no');
else:
    print('y');


# In[2]:

# Main Code started from here...........

from __future__ import print_function;

while True:
    string = raw_input().split(' ');
    if string[0] == '*':
        break;
    strlen = len(string);
    tot = True;
    firstchar = string[0][0].lower();
    #print(firstchar);
    for i in range(1,strlen):
        curr = string[i][0].lower();
        if(firstchar != curr):
            tot = False;
            break;
        firstchar = curr;
    if(tot == False):
        print('N');
    else:
        print('Y');

