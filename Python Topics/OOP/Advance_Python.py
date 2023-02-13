# Four Pillor of Object Oriented python
# (1) Encapsulation
# (2) Abstratction
# (3) Inheritance
# (4) Polymorphism





############# Date And Time #############

# from datetime import datetime
# from datetime import date
# from datetime import timedelta


# dt = datetime(year=2019, month=6, day=30)
# dtn = datetime.now()
# dtn = datetime.today()
# print(dt, end='\t\n')
# print(dtn)
# print(dtn.year)
# print(dtn.month)
# print(dtn.day)
# print(dtn.hour)

# cd = date.today()
# print(cd)
# print(cd.year)

# td = date.today()
# timedelta_v = timedelta(days = 10)
# # print(td + timedelta_v) # this is showing what will the date in next 10 days
# print(td - timedelta_v)

# d1 = date.today()
# timedelta_v = timedelta(days = 10)
# fd = d1 + timedelta_v

# print(d1)
# print(fd)
# print(fd < d1)
# print(fd > d1)
# print(fd == d1)
# print(fd != d1)


# dt = datetime.now() 
# print(dt)
# print()

# formated_date_name = dt.strftime("%A-%b-%Y")
# formated_date_number = dt.strftime("%d-%m-%Y")
# formated_date = dt.strftime("%B/%d/%Y")
# railway_time = dt.strftime("%H:%M:%S")
# home_time = dt.strftime("%I:%M:%S")
# print(formated_date_name)
# print(formated_date_number)
# print(formated_date)
# print(railway_time)
# print(home_time)

# import time

# for i in range(20):
#     print(i)
#     if (i == 10):
#         time.sleep(5)       # it means 5 seconds

# dob_alka = date(1970, 8, 1)
# dob_rohan = date(1997, 4, 8)
# dt = date.today()

# age = dt.year - dob_alka.year -((dt.month, dt.day) < (dob_alka.month, dob_alka.day))
# age = dt.year - dob_rohan.year -((dt.month, dt.day) < (dob_rohan.month, dob_rohan.day))
# print(age)


############# Lambda Function #############
'''
sum = lambda x:x+1
print(sum(5))
'''

'''
sum = lambda x,y: print(x+y)
sum(5,4)
'''

'''
add_sub = lambda x, y : (x+y, x-y)
a, b = add_sub(10,8)
print(f"add is : {a}\t and sub is: {b}")
'''
#### OR #####
'''
add_sub = lambda x, y : (x+y, x-y)
a = add_sub(10,8)
print(a)
'''

'''
add = lambda x=10, y=12 : print(x+y)
add()
'''
'''
f = lambda x : print(x**2)
f(5)
'''
'''
def g(num):
    return lambda n : print(num*n)
x = g(3)     # the 3 will asign to num = 3
x(10)     # the 10 will asign to n = 10
'''
'''
s = lambda x, y=5 : print(x+y)
s(25)
'''


############# Ternary Operator #############

'''
a = int(input('Enter First Number : '))
b = int(input('Enter Second Number : '))

print(f'{a} is greater than {b}') if a > b else print(f'{b} is greater than {a}')
'''

############# Comprehensions #############
'''
# Normal Function Type
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
even_no = []
for i in a:
    if i%2 == 0:
        even_no.append(i)
print(a)
print(even_no)
'''

'''
# Comprehensions Function Type
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
print(a)
even_no = [i for i in a if i%2==0]
print(even_no)
'''

'''
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
print(a)
print()
even = [i for i in a if i%2==0]
odd = [i for i in a if i%2!=0]
print(f"Odd Numbers : {odd}")
print(f"Even Numbers : {even}")
'''

'''
a = [1,2,3,4,5,6,7,8,9,10]
b = [11,12,13,14,15,16,17,18,19,20,21]
ls = [(i*j) for i in a for j in b]
print(ls)
'''

'''
a = [1,2,3,4,5,6,7,8,9,10]
b = [11,12,13,14,15,16,17,18,19,20]

ls = [(i,j) for i in a for j in b]
print(ls)
'''

# Comprehensions with Dictionary

'''
d = {}
for i in range(1,10):
    d[i] = i*i
print(d)
'''

'''
d = {i:(i*i) for i in range(1,10)}
print(d)
'''

'''
list1 = [x for x in range(1,8)]
list2 = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

dict1 = {key:value for (key,value) in zip(list1,list2)}
print(dict1)
'''

############# Magic Methods #############
'''
class Student:
    pass
s = Student()
print(dir(s))

# This all are Magic Methods
    # [
    #     '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
    #     '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
    #     '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    #     '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__'
    # ] 
''' 
''' 
class Collage:
    pass

dict1 = Collage()
print(dict1.__dict__)
dict1.name = 'Sohan'
dict1.surname = 'Chaudhari'
print(dict1.__dict__)
''' 
''' 
class Collage:
    """ Jaipur National University"""

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def __setattr__(self,name,value):    # if we define magic method in class then it call automatically
        print(f">>> You set {name} = {value}")
c = Collage('Akshay','Kumar')
print(c.__doc__)
print(c.__dict__)
''' 
''' 
class Collage:
    """ Jaipur National University"""

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def __setattr__(self,name,value):
        print(f">>> You set {name} = {value}")
        self.__dict__[name] = value
    
    def __getattr__(self, __name: str) -> Any:
        pass

c = Collage('Sunil','Shetty')
print(c.__doc__)
print(c.__dict__)
''' 

#############**************************** Map, Filter, Reduce Methods ****************************#############
############# Reduce
'''
from functools import reduce

a = [1,2,3,4,5,6,7,8,9,10]

operation = reduce(lambda n,m: n+m, a)
print(operation)
'''

############# Filter

'''
a = [1,2,3,4,5,6,7,8,9,10]

def num(x):
    if x>5:
        return True

f = list(filter(num, a))
print(f)
'''

############# Map
'''
a = [1,2,3,4,5,6,7,8,9,10]

m = list(map(lambda x: x+x, a))
print(m)
'''

'''
a = [1,2,3,4,5]
b = [6,7,8,9,10]

m = list(map(lambda x,y: x+y, a,b))
print(m)
'''

#############********************* Deep Copy, Shallow Copy *********************#############
'''
############ Deep Copy
from copy import deepcopy
a = [[1,2,3],[4,5,6],[7,8,9]]

print(id(a))
b = deepcopy(a)

print('List b : \t',b)
b[0][1] = 200
print('List b (modiied) : ',b)
print('List a : \t',a)
'''

'''
############# Copy
from copy import copy
a = [[1,2,3],[4,5,6],[7,8,9]]

b = copy(a)

print('List b : \t',b)
print(id(b))
b[0][1] = 200
print('List b (modiied) : ',b)
print('List a : \t',a)
'''