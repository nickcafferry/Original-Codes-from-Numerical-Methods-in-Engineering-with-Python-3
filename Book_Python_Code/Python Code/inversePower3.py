## module inversePower3
''' lam,x = inversePower3(d,c,s,tol=1.0e-6)
    Inverse power method applied to a symmetric tridiagonal
    matrix. Returns the eigenvalue closest to s
    and the corresponding eigenvector.
'''
from LUdecomp3 import *
import math
import numpy as np
from numpy.random import rand

def inversePower3(d,c,s,tol=1.0e-6):
    n = len(d)
    e = c.copy()
    cc = c.copy()
    dStar = d - s                  # Form [A*] = [A] - s[I]
    LUdecomp3(cc,dStar,e)          # Decompose [A*]
    x = rand(n)                    # Seed x with random numbers
    xMag = math.sqrt(np.dot(x,x))  # Normalize [x]
    x = x/xMag
    
    for i in range(30):               # Begin iterations    
        xOld = x.copy()               # Save current [x]
        LUsolve3(cc,dStar,e,x)        # Solve [A*][x] = [xOld]
        xMag = math.sqrt(np.dot(x,x)) # Normalize [x]
        x = x/xMag
        if np.dot(xOld,x) < 0.0:   # Detect change in sign of [x]
            sign = -1.0
            x = -x
        else: sign = 1.0
        if math.sqrt(np.dot(xOld - x,xOld - x)) < tol:
            return s + sign/xMag,x
    print('Inverse power method did not converge')
    return
