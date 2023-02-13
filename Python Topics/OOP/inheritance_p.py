################ Passing Members(variables) one class to another class ################
# class Student:
#     # cunstructor
#     def __init__(self, n, r):
#         self.name = n
#         self.roll = r

#     # instance method
#     def disp(self):
#         print("Student Name : ",self.name)
#         print("Student Roll : ",self.roll)


# class User:

#     # staic method
#     @staticmethod
#     def show(s):
#         print('User Name : ',s.name)
#         print('User R0ll : ',s.roll)
#         s.disp()

# stu = Student('Sohan', 101)
# user = User.show(stu)

################ Constructor in Inheritance ################
# By default , The Cunstuctor of parent class is available to the child class

# class Father():
#     def __init__(self, surname,money):
#         self.surname = surname
#         self.money = money
#         print('Father class Constructor Called...')

# class Son(Father):
#     def disp(self):
#         print(f"Child class Called...\tFather Surname is {self.surname} and he have {self.money} Money in Bank.")
# son = Son('Purane',100000)
# son.disp()

################ Constructor Overriding
# If we write constructor in both class child and parent, then parent class constructor will not available for child class
# Then the Child class constructor will call only

# class Father():
#     def __init__(self, surname,money):
#         self.surname = surname
#         self.money = money
#         print('Father class Constructor Called...')

# class Son(Father):
#     def __init__(self, name, surname,money):
#         self.name = name
#         self.surname = surname
#         self.money = money
#         print('Child class Constructor Called...')
#     def disp(self):
#         print(f"Son Name is and he have {self.money} Money in Bank.")
# son = Son('Rohan','Purane',100000)
# son.disp()

################ Constructor with Super Method (Call child and father class Constructor)
# If we write constructor in both class child and parent, but still we want to call parent class constructor

# class Father():
#     def __init__(self, surname,money):
#         self.surname = surname
#         self.money = money
#         print('Father Constructor class Called...')

# class Son(Father):
#     def __init__(self, name, surname,money):
#         self.name = name
#         super().__init__(surname,money)


#         print('Child Constructor class Called...')
#     def disp(self):
#         print(f"Son Name is {self.name} and Surname is {self.surname} and he have {self.money} Money in the Bank because of his Father.")
# son = Son('Rohan','Purane',100000)
# son.disp()




################ Instance Method OR call a method of class from different function which not belongs to class or outside of class ################


'''
class A:
    def do_somthing(self, x):
        print(f"do somthing {x}")
def main():
    a = A()
    a.do_somthing(1)
main()
'''
'''
class Calender:
    def __init__(self):
        self.event = []
    
    def add_event(self, event):
        self.event.append(event)
    
    def show_event(self):
        print(f"This is Event {self.event}")

def main():
    c = Calender()
    c.add_event('Get Some Achivements')
    c.show_event()
main()
'''

################ Multi-Level Inheritance
    # object
    #    |
    # Father
    #    |        # Example of Multi-Level Inheritance
    #   Son
    #    |
    #Grand_Son
    #    |
    #It can go on

# class Father():
#     def __init__(self,fmoney):
#         self.fmoney = fmoney

# class Son(Father):
#     def __init__(self, smoney, fmoney):
#         self.smoney = smoney
#         super().__init__(fmoney)

# class Grand_Son(Son):
#     def __init__(self, gsmoney, smoney, fmoney):
#         self.gsmoney = gsmoney
#         super().__init__(smoney, fmoney)
    
#     def show(self):
#         print(f"Father have {self.fmoney} in Bank")
#         print("\t\tAnd")
#         print(f"Son's Money {self.smoney} and Father's Money {self.fmoney} so now Son have {self.smoney + self.fmoney} Money")
#         print("\t\tAnd")
#         print(f"Grand_Son's Money {self.gsmoney} and Son's Money {self.smoney} and Father's Money {self.fmoney} so now Grand_Son have {self.gsmoney + self.smoney + self.fmoney} Money")
# son = Grand_Son(20,30,100)
# son.show()

################ Hierarchical Inheritance

# If one parent class have multiple child class then it will known as Hierarchical Inheritance

#                                     Father_Class
#                                           |
#         _____________________________________________________________________________
#         |             |             |               |               |               |
# Child_class1    Child_class2    Child_class3    Child_class4    Child_class5    Child_class6

'''
class Father():
    def __init__(self,fname):
        self.fname = fname

        print(f"Father Name is Shahaji Raje {self.fname}")


class Son_1(Father):
    def __init__(self, s1name, fname):
        self.s1name = s1name
        super().__init__(fname)
    
        print(f"Son_1 Name is {self.s1name} {self.fname}")

class Son_2(Father):
    def __init__(self, s2name, fname):
        self.s2name = s2name
        super().__init__(fname)

        print(f"Son_2 Name is {self.s2name} {self.fname}")

class Son_3(Father):
    def __init__(self, s3name, fname):
        self.s3name = s3name
        super().__init__(fname)

        print(f"Son_3 Name is {self.s3name} {self.fname}")

s1 = Son_1('Sambhaji Raje', 'Bhosale')
print()
s2 = Son_2('Shivaji Raje', 'Bhosale')
print()
s3 = Son_3('Venkoji Raje', 'Bhosale')
'''

'''
# If we want to call by function
class Father():
    def __init__(self,fname):
        self.fname = fname
    
    def showf(self):
        print(f"Father Name is Shahaji Raje {self.fname}")


class Son_1(Father):
    def __init__(self, s1name, fname):
        self.s1name = s1name
        super().__init__(fname)
    
    def shows1(self):
        print(f"Son_1 Name is {self.s1name} {self.fname}")

class Son_2(Father):
    def __init__(self, s2name, fname):
        self.s2name = s2name
        super().__init__(fname)

    def shows2(self):
        print(f"Son_2 Name is {self.s2name} {self.fname}")

class Son_3(Father):
    def __init__(self, s3name, fname):
        self.s3name = s3name
        super().__init__(fname)

    def shows3(self):
        print(f"Son_3 Name is {self.s3name} {self.fname}")

s1 = Son_1('Sambhaji Raje', 'Bhosale')
s1.showf()
s1.shows1()
print()
s2 = Son_2('Shivaji Raje', 'Bhosale')
s2.showf()
s2.shows2()
print()
s3 = Son_3('Venkoji Raje', 'Bhosale')
s3.showf()
s3.shows3()
'''

################ Multiple Inheritance
# Method Resolution Order(MRO)-> it search in Left to Right Manner
'''
# But this is not Professional way
class Kfather():
    def __init__(self,kfather):
        self.kfather = kfather
        print(f"Father of King is {self.kfather}")

class Kmother():
    def __init__(self,kmother):
        self.kmother = kmother
        print(f"Mother of King is {self.kmother}")

class King():
    def __init__(self,kname):
        self.kname = kname
        print(f"King Name is {self.kname}")

class Kingdome(Kfather, Kmother, King):
    def __init__(self,kingdome,kfather,kmother,kname):
        self.kingdome = kingdome
        Kfather.__init__(self,kfather)
        Kmother.__init__(self,kmother)
        King.__init__(self,kname)

        print(f"They made a Kingdome known as {self.kingdome}")
k = Kingdome('Swaraj', 'Shahaji Raje', 'Aai Jijau', 'Shivaji Maharaj')
'''

'''
class Kfather():                        #<---- Best Approach
    def __init__(self,kfather, **kwargs):
        super().__init__(**kwargs)
        self.kfather = kfather
        print(f"Father of King is {self.kfather}")

class Kmother():
    def __init__(self,kmother, **kwargs):
        super().__init__(**kwargs)
        self.kmother = kmother
        print(f"Mother of King is {self.kmother}")

class King():
    def __init__(self,kname, **kwargs):
        super().__init__(**kwargs)
        self.kname = kname
        print(f"King Name is {self.kname}")

class Kingdome(Kfather, Kmother, King):
    def __init__(self,kingdome,kf,km,kn):
        self.kingdome = kingdome
        super().__init__(kfather = kf,kmother = km,kname = kn)

        print(f"They made a Kingdome known as {self.kingdome}")
k = Kingdome('Swaraj', 'Shahaji Raje', 'Aai Jijau', 'Shivaji Maharaj')
'''
