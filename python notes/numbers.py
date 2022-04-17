from doctest import ELLIPSIS_MARKER
from winreg import EnableReflectionKey


x=1
# x is an integer
a=2.3
#a is a floating point number
c=2j+1
# c is a complex number

print(type(c))
print(type(a))
print(type(x))
b=float(x)
print(b)

g= 3/2
print(float(g))
# this allows for a division operation and the result not to be an integer, but I realized that only in Python 2 you need to do something like that. In Python 3 you can print(3/2)
print(3/2)
# You get 1.5, so that is something I need to remember

print(16/2)
print(3*(8/3))
print(6/2)
print(10*3)
print(2+6)
print(10-2)
# Here I am practicing operations in Python
"""
The next section will have more practice with numbers. However, this will pertain to the "Math Basics" Project
"""
table_value=x
# x is not supposed to be 1. I just needed a value for my variable table_value to equal.
import random
print(random.randrange(1,11)+table_value)
# this bit allows the tables to be created. Though I will probably use libraries and have the random of operation tables used, this is a great prelim step.

