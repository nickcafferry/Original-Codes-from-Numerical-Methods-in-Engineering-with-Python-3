## module householder
''' d,c = householder(a).
    Householder similarity transformation of matrix [a] to 
    tridiagonal form].

    p = computeP(a).
    Computes the acccumulated transformation matrix [p]
    after calling householder(a).
'''    
import numpy as np
import math

def householder(a): 
    n = len(a)
    for k in range(n-2):
        u = a[k+1:n,k]
        uMag = math.sqrt(np.dot(u,u))
        if u[0] < 0.0: uMag = -uMag
        u[0] = u[0] + uMag
        h = np.dot(u,u)/2.0
        v = np.dot(a[k+1:n,k+1:n],u)/h
        g = np.dot(u,v)/(2.0*h)
        v = v - g*u
        a[k+1:n,k+1:n] = a[k+1:n,k+1:n] - np.outer(v,u) \
                         - np.outer(u,v)
        a[k,k+1] = -uMag
    return np.diagonal(a),np.diagonal(a,1)

def computeP(a): 
    n = len(a)
    p = np.identity(n)*1.0
    for k in range(n-2):
        u = a[k+1:n,k]
        h = np.dot(u,u)/2.0
        v = np.dot(p[1:n,k+1:n],u)/h           
        p[1:n,k+1:n] = p[1:n,k+1:n] - np.outer(v,u)
    return p
      
                

