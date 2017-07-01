# -*- coding: utf-8 -*-
"""
Created on Sat Jul 01 21:38:42 2017

@author: Pranta Sarker
"""

from __future__ import print_function;
from random import *;

def pfn(x):
    print(x , end="\n");

def pf(x):
    print(x , end=" ");

def pf3n(x , y , z):
    print(x , y , z , end = "\n");    

def pf4n(a , b , c , d):
    print(a , b , c , d, end = "\n"); 

# introduction to dictionary, a beauty of great python

# dictionary is represented by {} -> curly barces

info = {
'first_name': 'pranta',
'last_name': 'sarker',
'occupation': 'student',
'age': 10 * 2 + 2,
'institution': 'neub',
'working on': 'python',
'comment': 'python is great',
'on_going': 'bekar',
'last say': 'okay sir'
}

pfn('>> Q. who are you ?');
pf3n('Me: this is' , info['first_name'] , info['last_name']);

pfn('>> Q. what you are doing now ?');
pf3n('Me: i am' , info['on_going'] , 'now');

pfn('>> Q. what did you do ?');
pf3n('Me: i was a' , info['occupation'] , ' ');

pfn('>> Q. how much age you are beloging now ?');
pf3n('Me: i am now' , info['age'], 'years old');

pfn('>> Q. which institution did you pass ?');
pf3n('Me: i am from' , info['institution'], ' ');

pfn('>> Q. in your study life, which language made you happy ?');
pf3n('Me: i got pleasure in', info['working on'] , ' ');

pfn('>> Q. do you have any comment about it ?');
pf3n('Me: i just want to say that,', info['comment'] , ' ');

pfn('>> Great! see you again :P');
pf3n('Me:' , info['last say'] , ' ');

print('-' * 70);

# another example of dictionary

print("DNA sequence: " , end=" ");

dna = {

1 : 'A' ,
2 : 'T',
3 : 'C',
4: 'G'
}

pf4n(dna[1] , dna[2] , dna[3], dna[4]);

n = 10;

print('get' , n , 'random nucleotides: ' , end="\n");

for i in range(0, n):
    x = randint(1 , 4);
    print(dna[x] , end = " ");
