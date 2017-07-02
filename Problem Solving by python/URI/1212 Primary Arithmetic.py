
# coding: utf-8

# In[3]:

# Author: Pranta Sarker

from __future__ import print_function;

while True:
    a , b = raw_input().split(" ");
    alist = [];
    blist = [];
    if a == '0' and b == '0':
        break;
    for i in a:
        alist.append(i);
    for i in b:
        blist.append(i);
    
    alist.reverse();
    blist.reverse();
    
    alen = len(alist);
    blen = len(blist);
    
    if(blen > alen):
        for i in range(alen , blen):
            alist += ['0'];
    else:
        for i in range(blen , alen):
            blist += ['0'];
    
    carry = cnt = 0;
    
    alen = len(alist); # update the length of alist
    blen = len(blist); # update the length of blist
    
    #print(alist,'; ' , alen ,  '\n', blist, '; ', blen);
    
    for i in range(0, alen):
        x = int(alist[i]);
        y = int(blist[i]);
        add = x + y;
        if(carry != 0):
            add += carry;
        #print('add=' , add , '\n');
        if(add > 9):
            cnt += 1;
            temp = str(add);
            carry = int(temp[0]);
            #print('carry = ' , carry , '\n');
        else:
            carry = 0;
    if(cnt == 0):
        print("No carry operation.")
    elif(cnt == 1):
        print( cnt, 'carry operation.');
    else:
        print( cnt,'carry operations.');

