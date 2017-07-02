
# coding: utf-8

# In[ ]:

# Author: Pranta Sarker
# URI 1279-Leap Year or Not Leap Year
# Verdict: AC


# In[ ]:

# Leap Year: num%4==0 or num%400==0 and num%100!=0
# Huluculu festival: num%15==0
# Bulukulu festival: num%55==0


# In[ ]:

# code start from here....


# In[ ]:

from __future__ import print_function;

nl = 0;

while True:
    try:
        year = input();
        
        if(nl != 0):
            print("");
        
        nl = 1;
        
        if(year%4==0 and (year%100!=0 or year%400==0)):
            print('This is leap year.');
            if((year % 15)==0):
                print('This is huluculu festival year.');
            if((year%55)==0):
                print('This is bulukulu festival year.');
        elif((year%15)==0):
            print('This is huluculu festival year.');
        else:
            print('This is an ordinary year.');
    except EOFError:
        break;

