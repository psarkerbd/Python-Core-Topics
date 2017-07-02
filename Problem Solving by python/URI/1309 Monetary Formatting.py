
# coding: utf-8

# In[ ]:

# Author: Pranta Sarker


# In[ ]:

# testing

from __future__ import print_function;

li = [];
n = raw_input();
for i in range(len(n)):
    li += [n[i]];
mon = [];
tmp = [];
#mon.reverse();
for i in range(len(n)-1, 0 , -1):
    tmp += li[i];
    mon += [li[i]];
    if(len(tmp) == 3):
        tmp = [];
        mon += [','];

ln = len(li);
mon += li[0];
mon.reverse();

for i in range(len(mon)):
    print(mon[i] , end=' ');


# In[ ]:

from __future__ import print_function;

#test = input();

#for i in range(test):
dollar = raw_input();
cent = input();
dlen = len(dollar);
dlist = [];
for i in range(dlen):
    dlist += [dollar[i]];
mon = [];
cnt = 0;
for i in range(dlen-1, 0, -1):
    cnt += 1;
    mon += [dlist[i]];
    if(cnt == 3):
        cnt = 0;
        mon += [','];
mon += [dlist[0]];
mon += ['$']
mon.reverse();
mon += ['.'];
#print('cent = ' , cent , end='\n');
if(cent >= 0 and  cent < 10):
        mon += ['0'];
for i in range(len(mon)):
        print(mon[i], end='');
print(cent, '');


# In[ ]:

#Code start from here....

from __future__ import print_function;

while True:
    try:
        dollar = raw_input();
        cent = input();
        dlen = len(dollar);
        dlist = [];
        for i in range(dlen):
            dlist += [dollar[i]];
        mon = [];
        cnt = 0;
        for i in range(dlen-1, 0, -1):
            cnt += 1;
            mon += [dlist[i]];
            if(cnt == 3):
                cnt = 0;
                mon += [','];
        mon += dlist[0];
        mon += ['$'];
        mon.reverse();
        mon += ['.'];
        if(cent >= 0 and cent < 10):
            mon += ['0'];
        for i in range(len(mon)):
            print(mon[i], end='');
        print(cent);
    except EOFError:
        break;

