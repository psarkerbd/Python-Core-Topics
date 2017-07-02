
# coding: utf-8

# In[ ]:

# Author: Pranta Sarker


# In[ ]:

# Verdict: AC


# In[ ]:

def GCD(a , b):
    if(b == 0):
        return a;
    return GCD(b , a%b);

while True:
    try:
        x , y , z = raw_input().split(' ');
        mylist = [];
        mylist.append(int(x))
        mylist.append(int(y));
        mylist.append(int(z));
        mylist.sort();
        #print mylist;
        a = mylist[0];
        b = mylist[1];
        c = mylist[2];
        triplet = primitive = False; 
        if(a*a + b*b == c*c):
            triplet = True;
        if(GCD(a , b)==1 and GCD(b , c)==1 and GCD(a , c)==1):
            primitive = True;
        if(triplet==True and primitive==True):
            print 'tripla pitagorica primitiva';
        elif(triplet==True and primitive==False):
            print 'tripla pitagorica';
        else:
            print 'tripla';
            
    except EOFError:
        break;

