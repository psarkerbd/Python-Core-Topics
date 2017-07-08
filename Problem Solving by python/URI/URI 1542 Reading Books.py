
# coding: utf-8

# In[2]:

# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from __future__ import print_function
while True:
    inp = raw_input().split(' ');
    if(inp[0] == '0'):
        break;
    Q = int(inp[0]);
    D = int(inp[1]);
    P = int(inp[2]);
    total = Q * D * P;
    page = total / abs(P - Q);
    if(page == 1):
        print(page , 'pagina');
    else:
        print(page, 'paginas');

