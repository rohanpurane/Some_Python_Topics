#(1)  Text file => charctors, strings , etc.
#(2)  Binary file => text, images, pdf, csv, video, audio, etc.


'''
# Just normal Func.
lst = []
for i in range(3):
    name = input('Enter Name : ')
    lst.append(name)
print(lst)
'''


'''
# creating txt file
f = open('file1.txt', mode='w')
f.write('Hello, How are you?')
f.close()
'''

########################### Text Mode And Binary Mode ###########################
'''
f = open('file1.txt', mode='w')
f.write('Hello,\n')
f.write('How are you?\n')
f.write('Tell me somthing?\n')
f.close()
print('Writting Success!')

f = open('file1.txt', mode='r')      # Text Read Mode
data = f.read()
print(data)
f.close()

f = open('file1.txt', mode='rb')     # Binary Read Mode
data = f.read()
print(data)
f.close()
print()
'''

'''
f = open('file1.txt','a')          # 'a' is use yo append data.
f.write('Jay Hanuman,\n')
f.close()
print('Writting Success!')

f = open('file1.txt', mode='r')      # Text Read Mode
data = f.read()
print(data)
f.close()
'''

########################### Some Func ###########################
'''
f = open('file1.txt', mode='r')      # Text Read Mode
data = f.read()
print(data)
print('The name of File is : ',f.name)
print('File is Readale : ',f.readable())
print('File is Writale : ',f.writable())
print('File is closed (Before close func) : ',f.closed)
f.close()
print('File is closed (After close func) : ',f.closed)
'''

'''
f = open('file2.txt', mode='x', encoding='utf-8')       # 'x' is use when if file is not created and we create and it using 'x'
                                                        # it will show error if file is already created
print('The name of File is : ',f.name)
print('File is Readale : ',f.readable())
print('File is Writale : ',f.writable())
print('File is closed (Before close func) : ',f.closed)
f.close()
print('File is closed (After close func) : ',f.closed)
'''


'''
f = open('file2.txt', mode='a+', encoding='utf-8')
print('The name of File is : ',f.name)
print('File is Readale : ',f.readable())
print('File is Writale : ',f.writable())
print('File is closed (Before close func) : ',f.closed)
f.close()
print('File is closed (After close func) : ',f.closed)
'''

'''
with open('img.jpg', mode='rb+') as f:
    data = f.read()
    print(data)
    print('The name of File is : ',f.name)
    print('The Mode of File is : ',f.mode)
    print('File is Readale : ',f.readable())
    print('File is Writale : ',f.writable())
    print('File is closed (Before close func) : ',f.closed)
    print('File is closed (After close func) : ',f.closed)
'''

########################### Check file exist or not ###########################

# import os

# print(os.path.isfile('img.jpg'))


########################### Writing and Reading data to file ###########################

'''
with open('file2.txt', 'w') as f:
    f.write('Jay Hanuman........!!!\n')
    f.write('Jay Hanuman........!!!\n')
    f.write('Jay Hanuman........!!!\n')
    f.close()
'''
'''
with open('file2.txt', 'w') as f:
    lst = ['Rahul\t','Raani\t','Raaja\t','Raana\t','Maharaaja\n']
    f.writelines(lst)
    f.close()
    print('Successfully written !')
'''
'''
with open('file2.txt', 'a') as f:
    lst = ['Rahul\t','Raani\t','Raaja\t','Raana\t','Maharaaja\n']
    f.writelines(lst)
    f.close()
    print('Successfully written !')
'''

# with open('file2.txt', 'r') as f:
#     data = f.read()
#     print(data)
#     f.close()

'''with open('file2.txt', 'a+') as f:
    print('tell is : ',f.tell())
    f.write('Mastani\t')
    f.seek(0)
    print('tell is : ',f.tell())
    data = f.read()
    print('tell is : ',f.tell())
    print(data)
f.close()'''


########################### Copy file content ###########################

'''
f1 = open('file1.txt','r')
f2 = open('file2.txt','w')

data = f1.read()
f2.write(data)
print(data)
f1.close()
f2.close()
'''

########################### with statement ###########################
# if we use 'with' statement then we don't need to close the file

'''
with open('file2.txt', 'a+') as f:
    print('Pointer of file : ',f.tell())
    f.write('Jay Bajrangvali\t')
    f.seek(0)
    print('Pointer of file : ',f.tell())
    data = f.read()
    print('Pointer of file : ',f.tell())
    print(data)
    print('Is file closed or not : ',f.closed)
print('Is file closed or not : ',f.closed)
'''

########################### Pickling and Unpickling ###########################
#                                     OR
########################### Serealization and Diserealization ###########################

'''
import pickle
from time import sleep

class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address

    def disp(self):
        print(f'Student Data : \n\tName : {self.name} \n\tRoll : {self.roll} \n\tAddress : {self.address}')

    
with open('Student.dat', mode='wb') as f:      #<= This is binary file 'Student.dat'
    stu1 = Student('Rahul',101,'Pune')
    pickle.dump(stu1, f)
    print('Pickling Done ...')
    print()
    sleep(2)
with open('Student.dat', mode='rb') as f:
    obj = pickle.load(f)
    print('Unpickling Data ... Wait for While.....')
    sleep(3)
    print('Unpickling Done ...')

    obj.disp()
'''
'''
import pickle
from time import sleep

class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address

    def disp(self):
        print(f'Student Data : \n\tName : {self.name} \n\tRoll : {self.roll} \n\tAddress : {self.address}')

n = int(input('Enter Number of Students : '))
with open('Student.dat', mode='wb') as f:
    for _ in range(n):
        name = input('Enter Name : ')
        roll = int(input('Enter Roll Number : '))
        address = input('Enter Address : ')
        stu1 = Student(name,roll,address)
        pickle.dump(stu1, f)
    print('Pickling Done ...')
    print()
    sleep(2)

with open('Student.dat', mode='rb') as f:
    print('Unpickling Data ... Wait for While.....')
    sleep(3)
    print('Unpickling Done ...')
    for _ in range(n):
        obj = pickle.load(f)
        obj.disp()
'''    
    
        

########################### Directory ###########################











########################### Practice ###########################


# with open('myfile.txt', 'w+') as f:
#     i = input('Enter Input : ')
#     f.write(i)