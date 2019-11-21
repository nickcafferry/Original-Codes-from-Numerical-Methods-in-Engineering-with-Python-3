#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[18]:


from numpy import dot


# In[19]:


from numpy import array


# In[3]:


def gaussElimin(a,b):
    n = len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k]!=0.0:
                lam =a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n]-lam*a[k,k+1:n]
                b[i]=b[i]-lam*b[k]
    for k in range(n-1,-1,-1):
        b[k] = (b[k]-dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b


# In[20]:


a = array([[1,1,1,1],[0,1,-1,-1],[0,0,-5,-8],[0,0,0,11]])


# In[21]:


b = array([[10],[-5],[-47],[44]])


# In[22]:


gaussElimin(a,b)


# In[23]:


a = array([[1,-2,2],[2,-3,-3],[4,1,6]])


# In[24]:


b = array([[-2],[4],[3]])


# In[25]:


gaussElimin(a,b)


# In[ ]:


from numpy import dot
from numpy import array
def gaussElimin(a,b):
    n = len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k]!=0.0:
                lam =a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n]-lam*a[k,k+1:n]
                b[i]=b[i]-lam*b[k]
    for k in range(n-1,-1,-1):
        b[k] = (b[k]-dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

