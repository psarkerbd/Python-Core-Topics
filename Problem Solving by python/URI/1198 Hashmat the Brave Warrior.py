# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:17:28 2017

@author: Pranta Sarker
"""
# python 2.7

while True:
    try:
        a , b = raw_input().split(' ');
        x = int(a);
        y = int(b);
        if x > y:
            ans = x - y;
        else:
            ans = y - x;
        print ans;
    except EOFError:
        break;
