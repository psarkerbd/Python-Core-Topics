# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 02:10:31 2017

@author: Pranta Sarker
"""

# Data Structure: list

import copy;
import bisect;

print "Hello World ! This is a list Data Structure";

# mylist [:] = [] # clear the list in python 2 versions
# list data structure is represented by bracket []

mylist = [1 , 2 , 3,] # this is a list

# append

mylist.append(4);
mylist.append(5);
mylist.append(6);

#mylist.append([7 , 8 , 9 , 10]);

#mylist.extend([i for i in mylist]);

#mylist.extend([mylist]);
#mylist = mylist;
#mylist.extend([7 , 8 , 9 , 10]);
mylist.extend([7 , 8 , 9, 10]);

print mylist;

# find the index of any element which is exist on mylist
# 0 base indexing

print "index = " , mylist.index(6);

# insert has 2 parameter, insert(index , value)

print "inserted new element on mylist: " , mylist;

# remove the last element by pop;

mylist.pop();
print "popped the last element: " , mylist;

# count any element how much occured

mylist.append(5);
print mylist;
print "5 has occured " , mylist.count(5) , " times";

# you can sort as ascending order the list to use sort method

mylist.sort();
print mylist;

# you can sort as descending order the list to use sort method

mylist.sort(reverse = True);
print mylist;

# you can simply reverse the list by using reverse method

mylist.reverse();
print mylist; 

# by using operators you ca also insert element
# + work as extend
# * how many times will be occured
mylist += [10];
mylist += [11];
mylist += [12];
print mylist;

mylist *= 2;
print mylist;

# slicing: list[first_index : last_index: step]

print mylist[4 : 10];
print mylist[: 10]; # index 0 to < 10
print mylist[10:]; # index 0 to last
print mylist[: : 3] # index 0 to last by step 1

# list line compresion
print [i for i in mylist if i%2==1];

#stack

stack = mylist; # copy mylist into stack
print "stack = ", stack;

stack.append(13);
print stack;

stack.pop();

print stack;

queue = stack; # stack cpoied into queue

queue.append(14);
print queue;

queue.pop(2); # pop the desird index
print queue;

# another way to copy a list into another list

mylist = copy.copy(queue);

print mylist;

mylist.insert(2, 3);
print mylist;

# another way is deepcopy, by this values can not make any change

queue = copy.deepcopy(mylist);
mylist.pop(2);
print "mylist = " , mylist;
print "queue = " , queue;

# insert any item on a sorted list

mylist.sort();

print "sorted mylist: " , mylist;

bisect.insort(mylist ,15);
print mylist;
# print "index = ", mylist.index(15) + 1; # 1 base

bisect.insort(mylist ,1);
print mylist;
# print "index = ", mylist.index(1) + 1;

# to know the index where that number is inserted

print "10 is inserted in ",bisect.bisect(mylist , 10),"th index of sorted list" ;
# 1 base indexing
