
# coding: utf-8

# In[ ]:

# Author: Pranta Sarker


# In[ ]:

def r(x , y):
    return (9 * x * x) + (y*y);
def bet(x , y):
    return 2*(x * x) + (25 * y * y);
def c(x , y):
    return  (-100 * x) + (y * y * y);

test = input();

for i in range(test):
    a , b = raw_input().split(" ");
    x = int(a);
    y = int(b);
    #print x , y;
    Rafa = r(x , y);
    Beto = bet(x , y);
    Carlos = c(x , y);
    if(Rafa > Beto and Rafa > Carlos):
        print 'Rafael ganhou';
    elif(Beto > Rafa and Beto > Carlos):
        print 'Beto ganhou';
    else:
        print 'Carlos ganhou';

