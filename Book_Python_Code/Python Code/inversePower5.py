## module inversePower5
''' lam,x = inversePower5(Bv,d,e,f,tol=1.0e-6).
    Inverse power method for solving the eigenvalue problem
    [A]{x} = lam[B]{x}, where [A] is pentadiagonal and [B]
    is sparse. User must supply the function Bv(v) that
    returns the vector [B]{v}.
'''
import numpy as np
from LUdecomp5 import *
import math
from numpy.random import rand

def inversePower5(Bv,d,e,f,tol=1.0e-6):  
    n = len(d)
    d,e,f = LUdecomp5(d,e,f)
    x = rand(n)                     # Seed x with random numbers
    xMag = math.sqrt(np.dot(x,x))   # Normalize {x}
    x = x/xMag
    for i in range(30):             # Begin iterations
        xOld = x.copy()             # Save current {x}
        x = Bv(xOld)                # Compute [B]{x}
        x = LUsolve5(d,e,f,x)       # Solve [A]{z} = [B]{x}
        xMag = math.sqrt(np.dot(x,x))  # Normalize {z}
        x = x/xMag
        if np.dot(xOld,x) < 0.0:    # Detect change in sign of {x}
            sign = -1.0
            x = -x
        else: sign = 1.0
        if math.sqrt(np.dot(xOld - x,xOld - x)) < tol:
            return sign/xMag,x
    print('Inverse power method did not converge')
