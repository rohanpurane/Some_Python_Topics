
########### Setter And Getter ###########
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     @property
#     def msg(self):
#         return f"{self.name} got grade {self.grade}"

#     @msg.setter
#     def msg(self, msg):
#         sent = msg.split(" ")
#         print(sent)
#         self.name = sent[0]
#         self.grade = sent[-1]

# stud1 = Student('nia', 'B')
# print('name : ',stud1.name)
# print('grade : ',stud1.grade)
# print(stud1.msg)
# print()
# stud1.msg = "amulya got grade A"
# print('name : ',stud1.name)
# print('grade : ',stud1.grade)
# print(stud1.msg)


############# @decorator #############
# def shahaji(func):
#     def jijau():
#         print('Rashtramata Jijau (Aau Saheb)')
#         return func()
#     print('Shahaji Raje Bhosale')
#     return jijau

# @shahaji
# def p_sambhaji():
#     print('Sambhaji Raje Bhosale(Pratham)')
# p_sambhaji()

# print('')

# @shahaji
# def shivaji():
#     print('Chatrapati Shivaji Maharaj')
# shivaji()

#####

# def ind(func):
#     def mh():
#         print('Maharashtra Rajya')
#         return func()
#     print('India Country')
#     return mh
# @ind
# def pn():
#     print('Pune City')
# pn()

############# ClassMethod #############
# class Mobile:
#     fp = 'Yes'   # To access this class variable we need @classmethod

#     def show_model(self):       # see this method doesn't print this class variable
#         print(self.fp)

#     @classmethod
#     def is_fp(cls):
#         return cls.fp

#     @classmethod
#     def changefp(cls):        # if we change the value of fp then it will reflect in all objects which make for class and also for all methods in class
#         cls.fp = 'window'
#         return cls.fp

 
# realme = Mobile()
# print(realme.is_fp())
# print('realme = ',realme.fp)
# iphone = Mobile()
# print('iphone = ',iphone.fp)
# iphone.changefp()
# print()
# print(realme.is_fp())
# print('realme = ',realme.fp)
# iphone = Mobile()
# print('iphone = ',iphone.fp)



################ @Static Method ################
# m = input('Enter Mobile Name : ')
# p = int(input('Enter Price Amount : '))
# class Mobile:
                            # when we want to pass some arguments(values) from outside the class and perform some action in the method.
#     @staticmethod
#     def show_model(m, p):
#         model = m
#         price = p
#         return f"Model : {model}, 'Price : {price}"
# mb = Mobile()
# show = mb.show_model(m, p)
# print(show)
