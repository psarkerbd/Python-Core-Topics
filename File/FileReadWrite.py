
# coding: utf-8

# In[ ]:

# Author: Pranta Sarker
# Problem: Finding a Motif in DNA


# In[ ]:

get_ipython().run_cell_magic(u'writefile', u'myfile.py', u"a = 20;\nb = 40;\nadd = a+b;\nprint 'add = ', ans;\nmul = a * b;\nprint 'mul = ' , mul;\nprint 'thats it, boss';")


# In[ ]:

get_ipython().magic(u'run myfile.py')


# In[ ]:

# The Main started from here.....

#file = open("Rosalind Finding a Motif in DNA.txt" , "w");

from __future__ import print_function;

s=raw_input();
t = raw_input();

slen = len(s);
tlen = len(t);

print (tlen , ' ' , slen);

for i in range(slen):
    tmp = s[i : tlen+i];
    #print (tmp);
    if(tmp == t):
        print(i+1, end=' ');


# In[ ]:

# Write on a text file

file = open("mfile.txt", "w");

a = 10;
b = 30;
add = a+b;
#print add;
file.write('a = %d, b = %d , add = %d' %(a , b , add));

file.close;


# In[ ]:

# Read a text file
file = open('test.txt' , 'w');
file.write('%d\n%d' %(10, 20));

file = open('test.txt',  'r');
a = file.readline(); # read as string
b = file.readline(); #read as string
a = int(a);
b = int(b);
add = a+b;
print add;

