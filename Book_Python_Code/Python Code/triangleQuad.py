## module triangleQuad
''' integral = triangleQuad(f,xc,yc).
    Integration of f(x,y) over a triangle using
    the cubic formula.
    {xc},{yc} are the corner coordinates of the triangle.
'''
import numpy as np

def triangleQuad(f,xc,yc):
    alpha = np.array([[1.0/3, 1.0/3.0, 1.0/3.0],  \
                      [0.2, 0.2, 0.6],            \
                      [0.6, 0.2, 0.2],            \
                      [0.2, 0.6, 0.2]])
    W = np.array([-27.0/48.0,25.0/48.0,25.0/48.0,25.0/48.0])
    x = np.dot(alpha,xc)
    y = np.dot(alpha,yc)
    A = (xc[1]*yc[2] - xc[2]*yc[1]      \
       - xc[0]*yc[2] + xc[2]*yc[0]      \
       + xc[0]*yc[1] - xc[1]*yc[0])/2.0
    sum = 0.0
    for i in range(4):
        sum = sum + W[i] * f(x[i],y[i])
    return A*sum
