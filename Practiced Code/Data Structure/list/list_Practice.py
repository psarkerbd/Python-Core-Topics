# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 20:25:19 2017

@author: Pranta Sarker
"""

import copy;
import bisect;
import sys;

def pfn(str):
    print(str);
def pf(str):
    sys.stdout.write(str);

# print "How many numbers are required: ",
# mylist[:] = []; # make clear the list
# sys.stdout.write("How many required: ");
pf ("How many required: ");
mylist = [];
N = input();
i = 1;

while i<=N:
    #print "Enter number:" ,
    # sys.stdout.write("Enter: ");
    pf ("Enter number: ");
    x=input();
    mylist.append(x);
    i+=1;

print "Your List is: ", mylist;

pfn("Indices of your data: ");

for i in mylist:
    print i , " at " , mylist.index(i), "th";
    
pfn("after Sorting your data looking like: ");

mylist.sort();

print mylist;

pfn("Now, indices are: ");

for i in mylist:
    print i , ' at ' , mylist.index(i) , 'th';
    
#pfn("Reverse order of your Sorted data: ");

#mylist.sort(reverse = True);
#print mylist;

pfn('Do you want to any number in Sorted list: Press(1) for YES (2) for Other');

typ = input();

if typ == 1:
    pf('Enter Number: ');
    x = input();
    bisect.insort(mylist , x);
    print mylist;
    print "position =", mylist.index(x) , ' koto tomo = ' , bisect.bisect(mylist , x);
else:
    print mylist;

pf('Enter a number you want to delete: ');
x = input();
fl = 0;
for i in mylist:
    if x == i:
        mylist.remove(x);
        fl = 1;

if fl==1:
    pf('Now your list are: ');
    print mylist;
else:
    print 'Sorry!' , x, ' is not in the list';

 print 'Now your list are: ', mylist;

 pf("Take the even numbers from your list: ");

 print [i for i in mylist if i%2==0];
 
 
 ###### That's it ##############
