Link: http://localhost:8888/notebooks/A%20Folder/Operation.ipynb

# Code
# Developed on jupyter
# UDate: 24.jun.17
# UTime: 5.09 AM



# coding: utf-8

# In[4]:

#! python


# In[4]:

# output function
def ot(x):
    print "Result = ",x;


# In[5]:

# function for choice

def op(typ):
    
    if typ >= 1 and typ <= 4:
        first = input("Enter the First Element: ");
        second = input("Enter the Second Element: ");
    else:
        print "Error!";
    
    if typ == 1:
        ans = first + second;
        ot(ans);
        
    elif typ == 2:
        if first > second:
            ans = first - second;
            ot(ans);
        else:
            ans = second - first;
            ot(ans);
    elif typ == 3:
        ans = first * second;
        ot(ans);
    elif typ == 4:
        
        if first > second:
            ans = first / second;
            ot(ans);
        else:
            ans = second / first;
            ot(ans);


# In[13]:

# Run this Cell

print "How many operations nedded: ";
n = input();

print("Choise (1) for Addition\nChoise (2) for Absolute Subtraction\nChoise (3) for Multiplication\nChoise (4) for valid Division\n");

val = 1;

while val <= n:
    choise = input();
    op(choise);
    val += 1;

