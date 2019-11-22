#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# Core Python

# Variables

# In[3]:


b = 2 # b is integer type
print (b)
b = b*2.0 # Now b is float type
print (b)


# Strings

# In[5]:


string1 = 'Press return to exit'
string2 = 'the program'
print (string1+''+string2) #Strings are concatenated with the plus + operator
print(string1[0:12])


# s = 'Press return to exit'
# s[0] = 'p' # TypeError: 'str' object does not support item assignment

# Tuples

# In[12]:


rec = ('Smith','John',(6,23,68))
lastName,firstName,birthdate = rec
print(firstName)
birthYear = birthdate[2]
print(birthYear)
name = rec[1]+''+rec[0]
print(name)
print(rec[0:2])


# Lists

# In[13]:


a = [1.0,2.0,3.0]
a.append(4.0)
print(a)
a.insert(0,0.0)
print(a)
print(len(a))
a[2:4]=[1.0,1.0] #Modify the selected elements
print(a)


# In[14]:


a = [1.0,2.0,3.0]
b =a #if a is a mutable object, this assignment statement make any chnages to b be reflected in a
b[0] = 5.0
print(a)
c = a[:] # This is an indepent copy of a list a.
c[0] =1.0
print(a)


# In[19]:


a = [[1,2,3],[4,5,6],[7,8,9]] #Matrices can represented as nested lists with each row being an element of the list.
print (a[1])
print (a[1][2])
print (a) # Matrices 

Arithmetic Operators
# In[22]:


s = 'Hello'
t = 'to you'
a = [1,2,3]
print(3*s)
print(3*a)
print(a+[4,5])
print (s+t)
print (str(3)+s) # 'str' is needed here.Ohterwise,it winds up with unsupported operand types for +: 'int' and 'str'


# In[23]:


import numpy


# In[31]:


import numpy
a = numpy.sinh(3.14159)
b = numpy.cosh(3.14159)
print(a,b)
a +=b
print(a)

a = numpy.sinh(3.14159)
a -=b
print(a)

a = numpy.sinh(3.14159)
a*=b
print(a)

a = numpy.sinh(3.14159)
a/=b
print(a)

a = numpy.sinh(3.14159)
a%=b
print(a)

Comparison Operators
# In[32]:


a = 2
b = 1.99
c = '2'
print(a>b)
print(a==c)
print(a>b) and not(a!=c)
print(a>b) or (a==b)

Conditionals
# In[34]:


def sign_of_a(a):
    if a < 0.0:
        sign = 'negative'
    elif a > 0.0:
        sign = 'positive'
    else:
        sign = 'zero'
    return sign
a = numpy.tanh(3.14159)
print(a)
print ('a is ' + sign_of_a(a))

Loops
# In[36]:


nMax = 5
n = 1
a = [] # Create an empty list
while n < nMax:
    a.append(numpy.sinh(n))
    n = n+1
print(a)


# In[42]:


n =1
a =[]
nMax = 5
for n in range(1,nMax):
    a.append(numpy.sinh(n))
print(a)


# In[50]:


list = ["Jack", "Jill","Tim","Dave"]
name = str(input('Type a name: ')) #Python input prompt
for i in range(len(list)):
    if list[i] == name:
        print(name, 'is number',i+1,'on the list')
        break
else:
    print(name,'is not on the list')


# Type Conversion

# In[59]:


a = 5
b = -3.6
d = '4.0'
print(a+b)
print(int(b))
print(complex(a,b))
print (float(d))
print(eval(d))

Reading Input
# In[60]:


a = input('Input a: ')
print(a,type(a))
b = eval(a)
print(b,type(b))


# In[ ]:




