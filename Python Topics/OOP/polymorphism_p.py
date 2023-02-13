
#############***************** Polymorphism => Start*****************#############
############# Duck Typing #############

# class Duck:
#     def walk(self):
#         print('thapak thapak thapak thapak')

# class Horse:
#     def walk(self):
#         print("tabdak tabdak tabdak tabdak")

# def myfunction(s):
#     s.walk()

# d = Duck()
# myfunction(d)

# h = Horse()
# myfunction(h)


############# Strong Typing #############
# for this we use function => hasattr

# class Duck:
#     def walk(self):
#         print('thapak thapak thapak thapak')

# class Horse:
#     def walk(self):
#         print("tabdak tabdak tabdak tabdak")

# class Cat:
#     def talk(self):
#         print('meaow meaow meaow meaow')

# def myfunction(s):
#     if hasattr(s, 'walk'):
#         s.walk()
#     elif hasattr(s, 'talk'):
#         s.talk()
#     else:
#         print('oops, somthing went wrong !!!')

# d = Duck()
# myfunction(d)
# print()
# h = Horse()
# myfunction(h)
# print()
# c = Cat()
# myfunction(c)


############# Method Overloding #############
# if a method can perform more than one task, then it is known as method overloading

# class Myclass():
#     def sum(self, a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             s = a+b+c
#             return s
#         elif a!=None and b!=None and c==None:
#             m = a*b
#             return m
#         elif (a!=None and b==None and c==None) and a>1:
#             d = a//2
#             return d
#         else:
#             return "Somthing went wrong"    

# obj = Myclass()
# print(obj.sum(10,20,30))
# print(obj.sum(10,20))
# print(obj.sum(10))


############# Method Overriding #############
# if we write moethod in both classes(parent and child) then, parent class method will not work only child class method will execute
# so if we have same name of method in both class then how to call both of them

# class Add:
#     def result(self, x, y):
#         print('Addition :', x+y)

# class Multi(Add):
#     def result(self, a, b):
#         super().result(a, b)
#         print('Multiplication : ', a*b)

# m = Multi()
# m.result(10, 20)


############# Operator Overloding #############
# if any operator performs additional action other then what it is meant for, it is knows as Operator Overloding
# operators : +, -, *, /,%, &
# __add__(self, other)      +
# __sub__(self, other)      -
# __mul__(self, other)      *
'''
if we write:
print(10+20)
print('Hello '+'World')

then behind the scene it works like this
print(int.__add__(10,20))
print(str.__add__('Hello ','World'))
like this other operators also perform their operations
'''
# By defalt it calcualte or concatinate in integer aither string but if we want to calculate object then we use Operator Overloading

'''
class A:
    def __init__(self, x):
        self.x = x
    
    def __add__(self, other):
        return self.x + other.x


class B:
    def __init__(self, x):
        self.x = x
    def __sub__(self, other):
        return self.x - other.x
a = A(100)
b = B(200)
print(a+b)  # if we want call class A then mention a first
print(b-a)  # if we want call class B then mention b first
'''
############# Astract Class & @abstractmethod and Concrete Method #############
'''
from abc import ABC, abstractmethod


class Vehical(ABC):

    def __init__(self, fuel, average):
        self.fuel = fuel
        self.average = average
    
    @abstractmethod
    def engine(self):       #<----- Abstract Method
        pass
    def but(self):          #<----- Concrete Method
        print('And the Servicing is mandatory in every month...')

class Nexon(Vehical):

    def __init__(self, fuel, average, vname):
        self.vname = vname
        super().__init__(fuel, average)

    def engine(self):
        if self.fuel > 1:
            self.run = self.fuel * self.average
        print(f"This {self.vname} run {self.run} km in {self.fuel}ltr of Fuel")
 
n = Nexon(2, 8, 'Nexon')
n.engine()
n.but()
print()

class BMW(Vehical):

    def __init__(self, fuel, average, vname):
        self.vname = vname
        super().__init__(fuel, average)

    def engine(self):
        if self.fuel > 1:
            self.run = self.fuel * self.average
        print(f"This {self.vname} run {self.run} km in {self.fuel}ltr of Fuel")
 
b = BMW(10, 50, 'BMW')
b.engine()
b.but()
'''
'''
from abc import ABC, abstractmethod

class Defence_Force(ABC):
    def __init__(self, location):
        self.location = location

    @abstractmethod
    def assets(self):
        pass

    @abstractmethod
    def enamy(self):
        pass

    def area(self):
        print(f"The war location is {self.location}")

class Army(Defence_Force):

    def __init__(self, force, wepon, location):
        self.force = force
        self.wepon = wepon
        super().__init__(location)

    def assets(self):
        print(f"Defence Force is {self.force} and they have {self.wepon} wepons.")
 
    def enamy(self):
        print(f"Becuase enamy is {self.location}")
a = Army('Indian Army', 'AK_56', 'China')
a.assets()
a.area()
a.enamy()
print()

class AirForce(Defence_Force):

    def __init__(self, force, wepon, location):
        self.force = force
        self.wepon = wepon
        super().__init__(location)

    def assets(self):
        print(f"Defence Force is {self.force} and they have {self.wepon}")

    def enamy(self):
        print(f"Becuase enamy is {self.location}")
a = AirForce('Indian AirForce', 'ChoperJet', 'Saudi Arebia')
a.assets()
a.area()
a.enamy()
print()

class Navy(Defence_Force):

    def __init__(self, force, wepon, location):
        self.force = force
        self.wepon = wepon
        super().__init__(location)

    def assets(self):
        print(f"Defence Force is {self.force} and they have {self.wepon}")

    def enamy(self):
        print(f"Becuase enamy is {self.location}")
a = Navy('Indian Navy', 'Virat Submarine', 'America')
a.assets()
a.area()
a.enamy()
'''

# if their is not any concrete method  in abstract class only @abstractmethod is available then this class is known as Interface

