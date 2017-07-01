# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 21:39:32 2017

@author: Pranta Sarker
"""

from __future__ import print_function
# touple is faster than list

import sys;

def pfn(x):
    print(x , end=" ");

def pf(x):
    sys.out.write(x);
    
#N = input('How many numbers: ');

# make an emty touple

tpl1 = (1 , 2 , 3 , 13); 

#for i in range(N):
    #x = input('Enter a number: ');
    #tpl += (x , ); # insert a value on touple;

#pfn("Your existing touple:");
#print tpl;

# some built-in method for touple

#mytpl = (3 , 5 , 7 ,8 , 20);
tpl2 = tpl1;

ret =  cmp(tpl1 , tpl2);
if ret == 1:
    pfn('Matched');
else:
    pfn('Not matched');
# cmp retutn -1 if all the valus of tpl1 and tpl2 are not same
# cmp retutn 0 otherwise

# find the length of a tuple
# print len(tpl);

# find the maximum element on the tuple;
#print 'tpl1 elements: ';
print("tpl1 elements are: ", tpl1 , end="\n");

#print 'max element is: ' , max(tpl1);

# find the minimum value on tuple

#print 'minimum value is: ' , min(tpl1);

# convert a list into a tuple;

mylist = [100, 200, 345, 449, 500];

#print 'this is a list: ' , mylist;

tpl3 = tuple(mylist);

#print 'this is a touple:' , tpl3;

# Access the values of a tuple

size = len(tpl3);

#print size;

#print tpl3[0:];

# do some operation on tuple

add = 0;

for i in tpl3:
    if i%2==0:
        add += i;

#print 'summation of tuple:' , sum(x);
#print 'summation of even numbers in tuple: ', add;

# cummulative sum in tuple;

# take a tuple

x = tpl3[0];
#print x;

cum_sum = ();

cum_sum += (x,);

add = x;

# size is the size of tpl3

# i = 2;

for i in range(1 , size):
    cum_sum += (cum_sum[i-1] + tpl3[i] , );

print ('Cumulative sum elements are: ', end=" ");

for i in cum_sum:
    print(i , end=" ");
    
print(" ");

#tpl4 = (1 , 4 , 5 , 6 , 5);

#print("5 has " , tpl4.count(5), " times in tpl4" ,  end=" ");

#size = len(tpl4);

# bsically any tuple does not assign any element
# so, that's why you have to make it a list and then
# you may assign any element on this list

li = [1 , 2 , 5 , 6 , 5];

print("list elements are: " , li , end=" ");

for i in range(0 , len(li)):
    if li[i]==1:
        li[i]=2;
    elif li[i]==5:
        li[i]=6;
    elif li[i]==6:
        li[i]=7;
    else:
        continue;

print(" ");

tpl4 = tuple(li);

print("Now tpl4 elements are: " , tpl4 , end=" ");

##### That's it !! #########