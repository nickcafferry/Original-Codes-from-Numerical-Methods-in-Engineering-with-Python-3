Chapter 1 is not a comprehensive manual of Python. Rather, it aims to bring you up to speed with sufficent information about python so that you can pick up the rest as you go. Presumably, you know something about another computer language.

Python is an object-oriented language (Fun fact: its name is derived from the British television show Monty Python's Flying Circus). Python is an excellent scripting language for enigeering applications. Very elegant and considerably more widespread than Fortran.

Python programs are not compiled into machine code, but are run by an interpreter (the python interpreter also compiles byte code, which helps to speed up execution somewhat.). Therefore, Python, as one of interpreted language, can be tested and debugged quickly, allowing users to concentrate more on the principles behind the program. 

Python programs can be developed in a much shorter time than equivalent Fortran or C programs. However, python applications cannot stand alone. That is, a Python program cannot be run without the help of Python interpreter.

Advantages of Python:
1. Open-source software, 'free', included in most Linux distributions;
2. Avaiable for Linux,Unix,Windows, MacOS etc. Interchangable within two different systems;
3. Easy to learn and more readable than other languages;
4. Its extensions and itself are easy to install.

Java and C++ have a great impact on the development of python, Python is also similar to MATLAB. Python implements the usual concepts of object-oriented languages such as classes, methods, inheritance etc.

You can find 'the equivalent Python function' on the website (https://github.com/nickcafferry/Original-Codes-from-Numerical-Methods-in-Engineering-with-Python-3/blob/master/GaussElimin.py)

You can also find Matlab codes (https://github.com/nickcafferry/Original-Codes-from-Numerical-Methods-in-Engineering-with-Python-3/blob/master/GaussElimin_matlab_code.m) and try to run it on online Octave websites (https://octave-online.net/, https://www.tutorialspoint.com/matlab/try_matlab.php, https://www.tutorialspoint.com/execute_matlab_online.php)

Below are some comments on python codes.

from numpy import dot
# The command from numpy import dot instructs the interpreter to load the function dot (i.e., computes the dot product of two vectors) from the module numpy. 
from numpy import array
# import array
def gaussElimin(a,b):
# The colon(:) operator, known as the slicing operator in Python, works the same way it does in MATLAB and Fortran90(defines a selection of an array)
    n = len(b)
    for k in range(0,n-1):
# The differences in the ranges of k in python and MATLAB reflect the native offsets used for arrays. In Python, all sequences have zero offset while in MATLAB the native offset is 1.
        for i in range(k+1,n):
            if a[i,k]!=0.0:
                lam =a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n]-lam*a[k,k+1:n]
                b[i]=b[i]-lam*b[k]
    for k in range(n-1,-1,-1):
        b[k] = (b[k]-dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
