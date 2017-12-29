# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:14:47 2017

@author: Pranta Sarker
"""

#python 2.7.11

from __future__ import print_function

f = open("sample.txt");

wfile = open("dic.txt", "w");

mydict = {};
charlist = [];
S = set();

for line in f:
    #wfile.write(line);
    for i in range(len(line)):
        S.add(line[i]);
        #mydict.setdefault(line[i], []).append(0);

print(S);
print("Unique Caharcters are: ", len(S));

f.close();
wfile.close();
