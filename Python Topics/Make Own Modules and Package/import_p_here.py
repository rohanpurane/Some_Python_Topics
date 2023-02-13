################### Let's Start to Use Our Own Package ###################


# import Geometry.area
# import Geometry.area as A
from Geometry.area import circle
from Geometry.volume import cube, cuboid

'''
print(f"Area of Circle : {Geometry.area.circle(5)}")
print(f"Area of Circle : {A.circle(5)}")
'''

'''
n = int(input('Enter Radius of Circle : '))
def myfun(n):
    return circle(n)
print(myfun(n))
'''


################################################################


'''
l = int(input('Enter Lenght of Cuboid : '))
w = int(input('Enter Width of Cuboid : '))
h = int(input('Enter Height of Cuboid : '))
def myfun(l, w, h):
    return f"Area of Cuboid is {cuboid(l, w, h)}"
print(myfun(l, w, h))
'''

'''
# if we to print info of module in python shell ->
>>> import Geometry
>>> help(Geometry)
Help on package Geometry:

NAME
    Geometry

PACKAGE CONTENTS
    area
    volume

FILE

=>  we can see there is no information available so to add some in formation go to 
    package files and add some info.

################################################################

=> After mentioning some information

>>> import Geometry.area
>>> help(Geometry.area)
Help on module Geometry.area in Geometry:

NAME
    Geometry.area - This package is made by the Programmer named Rohan.

FUNCTIONS
    circle(radius)

    rectangle(lenght, width)
        You can get Area of Rectangle with the use of this Function

FILE

################################################################


>>> from Geometry.area import circle
>>> dir(circle) 
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', 
'__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__get__','__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', 
'__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> 
'''