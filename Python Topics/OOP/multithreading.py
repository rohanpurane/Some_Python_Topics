# import threading
# from threading import Thread, current_thread


# After executing any programe one thread run everytime, this thread is knowen as Main-Thread.
# To check this thread =>
'''
t = threading.current_thread().getName()
print('GeekyShows')
print(t)
'''

# We have Three ways to create thread =>

# (1)  Creating a Thread without using a class.
'''
def disp(a):
    print("Thread Running ", a)
t = Thread(target=disp, args=(10,))
t.start()
'''

# After executing any programe one thread run always at very first,
# To check this thread =>
# We are Using MultiThreading Now.
'''
def disp():
    print("Thread Running ")
t = Thread(target=disp)
k = Thread(target=disp)
t.start()
k.start()

for i in range(5):
    print('Main Thread')
'''

'''
def disp():
    for i in range(5):
        print("Child Thread Running ",i)
t = Thread(target=disp)
t.start()

for i in range(5):
    print('Main Thread Running',i)
'''

# Set and Get Thread Name =>

# current_thread()
# getName()
# setName()
# @property
# import threading
# from threading import Thread, current_thread

'''
def disp():
    # print("Child Thread Object", current_thread())
    print("Child Thread Object", current_thread().getName())
    current_thread().setName('Doc Thread')
t = Thread(target=disp)
t.start()
print()
# print("Main Thread", current_thread())
print("Main Thread", current_thread().getName())
current_thread().setName('Main Main Thread')
'''
'''
def disp():
    print("Child",current_thread())
t = Thread(target=disp,name='User Defined Thread')
t.start()
print("Main",current_thread().name)
'''

# (2)  Creating a Thread by creating a child class to Thread class.
# from threading import Thread

# Here we are overriding 'run' Method from 'Thread' class
'''
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print('Child Thread Running')
t = Mythread()
t.start()
# print(t.name)
for i in range(5):
    print('Main Thread Running')
'''
# If we want to organize our threads, like which threads will run first then use 'Join' method
'''
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print('Child Thread Running')
t = Mythread()
t.start()
t.join()
# print(t.name)
for i in range(5):
    print('Main Thread Running')
''' 

####### Thread Child class with Cunstructor
# We are importing Thread class cunstrocture by using 'Thread.__init__(self):'

''' 
class Mythread(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        print('Cunstructor Thread', a)
    def run(self):
        print('Run Thread')
t = Mythread(10)
t.start()
print('Main Thread')
''' 

# (3)  Creating a Thread without creating a child class to Thread class.
''' 
from threading import Thread, current_thread


class Mythread:
    def disp(self, a, b):
        print('My Custom Thread', a, b)
t = Mythread()
t = Thread(target=t.disp, args=(10, 20))
t.start()

print('Main thread',current_thread().name)
''' 

####################################################################
''' 
# Single Tasking using threads
from threading import Thread
from time import sleep

class MyExam:
    def solve_questions(self):
        self.q1()
        self.q2()
        self.q3()
        self.q4()
    def q1(self):
        print('Question 1 Solved')
        sleep(3)
    def q2(self):
        print('Question 2 Solved')
        sleep(3)
    def q3(self):
        print('Question 3 Solved')
        sleep(3)
    def q4(self):
        print('Question 4 Solved')
        sleep(3)
e = MyExam()
t = Thread(target=e.solve_questions)
t.start()
''' 
####################################################################

# MultiTasking using Multiple Threads

# from threading import Thread, current_thread


'''
class Hotel:
    def __init__(self, t):
        self.t = t

    def food(self):
        for i in range(1, 6):
            print(self.t, i)
h1 = Hotel('Take Order From Table')
h2 = Hotel('Serve Order To Table')

t1 = Thread(target=h1.food)
t2 = Thread(target=h2.food)

t1.start()
t2.start()
'''
''' 
class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat

    def reserve(self, need_seat):
        print(f'Available Seats : {self.available_seat}')
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is allocated for {name}')
            self.available_seat -= need_seat
            print(f'Remaining Seats : {self.available_seat}')
        else:
            print('Sorry! All seats has allocated')
f = Flight(6)
t1 = Thread(target= f.reserve, args=(1,), name= 'Rahul')
t2 = Thread(target= f.reserve, args=(1,), name= 'Sonam')
t3 = Thread(target= f.reserve, args=(1,), name= 'Pratap')
t1.start()
t1.join()
t2.start()
t3.start()
''' 

##############################################################################
# Thread Synchronization using  Lock
'''
from threading import *
import time

class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = Lock()

    def reserve(self, need_seat):
        self.l.acquire()
        print(f'Available Seats : {self.available_seat}')
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is allocated for {name}')
            self.available_seat -= need_seat
            time.sleep(2)
        else:
            print('Sorry! All seats has allocated')
        self.l.release()
f = Flight(2)
t1 = Thread(target= f.reserve, args=(1,), name= 'Rahul')
t2 = Thread(target= f.reserve, args=(1,), name= 'Sonam')
t3 = Thread(target= f.reserve, args=(1,), name= 'Pratap')
t1.start()
t2.start()
t3.start()
print('Main Thread')
'''


##############################################################################
# Thread Synchronization using  RLock

from threading import *
import time

class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = RLock()
        # print(self.l)

    def reserve(self, need_seat):
        self.l.acquire()
        # print(self.l)
        print(f'Available Seats : {self.available_seat}')
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is allocated for {name}')
            self.available_seat -= need_seat
            time.sleep(2)
        else:
            print('Sorry! All seats has allocated')
        self.l.release()
f = Flight(7)
t1 = Thread(target= f.reserve, args=(1,), name= 'Rahul')
t2 = Thread(target= f.reserve, args=(1,), name= 'Sonam')
t3 = Thread(target= f.reserve, args=(1,), name= 'Pratap')
t1.start()
t2.start()
t3.start()
print('Main Thread')


##############################################################################
# Thread Synchronization using  Semaphore and BoundedSemaphore
'''
from threading import *
import time

class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        # self.l = Semaphore(2)
        self.l = BoundedSemaphore(1)
        # print(self.l)

    def reserve(self, need_seat):
        self.l.acquire()
        # print(self.l)
        print(f'Available Seats : {self.available_seat}')
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is allocated for {name}')
            self.available_seat -= need_seat
            time.sleep(2)
        else:
            print('Sorry! All seats has allocated')
        self.l.release()
        # print(f'Remaining Seats : {self.available_seat}')
f = Flight(7)
t1 = Thread(target= f.reserve, args=(1,), name= 'Rahul')
t2 = Thread(target= f.reserve, args=(1,), name= 'Sonam')
t3 = Thread(target= f.reserve, args=(1,), name= 'Pratap')
t4 = Thread(target= f.reserve, args=(1,), name= 'Prithvi')
t1.start()
t2.start()
t3.start()
t4.start()
print('Main Thread')
'''

########################################## Thread Communication ##########################################
# Thread Communication by Event
'''
from threading import *
from time import sleep

def light_switch():

    e.set()
    print('Green Light ON \n')
    sleep(3)
    print('Red Light ON')
    e.clear()
def traffic():
    e.wait()
    while e.is_set():
        print('You can Go........')
        sleep(.5)
    print('Programe Done')

e = Event()
t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)
t1.start()
t2.start()
'''
################################### Thread Communication by Condition Variable

'''
from threading import *
from time import sleep

lst = []

def produce():
    cv.acquire()
    for i in range(1, 9):
        lst.append(i)
        sleep(1)
        print('Item Produce......')
    cv.notify()
    cv.release()
def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print(lst)

cv = Condition()
t1 = Thread(target=produce)
t2 = Thread(target=consume)

t1.start()
t2.start()
'''

################################### Thread Communication by Queue
'''
from threading import *
from queue import Queue
from time import sleep

class Producer:
    def __init__(self):
        self.q = Queue()

    def produce(self):
        for i in range(1,6):
            print('Item Produced : ',i)
            self.q.put(i)
            sleep(1)

class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        for i in range(1, 6):
            print('Item Recieved : ', self.prod.q.get(i))

p = Producer()
c = Consumer(p)
t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)
t1.start()
t2.start()
'''

################################### Daemon Thread ###################################

# from concurrent.futures import thread
# from threading import Thread, current_thread
# from time import sleep

'''
def disp():
    print("Daemon Thread")

t1 = Thread(target=disp)
print('Before : ',t1.isDaemon())
t1.setDaemon(True)
print('After : ', t1.isDaemon())
t1.start()
'''
'''
def disp():
    print("Daemon Thread")

t1 = Thread(target=disp)
print('Before : ',t1.daemon)
t1.daemon = True
print('After : ', t1.daemon)
t1.start()
'''

# Main Thread is always None-Thread
'''
mt = current_thread()
print(mt.getName())
print(mt.daemon)
'''

# it depends on the parent thread that a thread is daemon or none-daemon
# and if parent-thread is daemon-thread then the child-thread is also a daemon-thread
# to make daemon thread we need to setDeamon = True to a object of class or func. before using the start() 
'''
def disp():
    print('Disp Function')
    t2 = Thread(target=show)
    print('T2 Thread : ', t2.daemon)
    t2.start()

def show():
    print('Show Function')

# Main Thread Start
mt = current_thread()
print(mt.getName()) 
print(mt.daemon)

# Child Thread Start(t1)
t1 = Thread(target=disp)

print('T1 Before : ',t1.daemon)
t1.daemon = True
print('T1 After : ', t1.daemon)
t1.start()
t1.join()
'''


'''
# without using daemon thread
def teacher():
    for i in range(1, 11):
        print('Teaching Session : ',i)
        sleep(1)
t1 = Thread(target=teacher)
t1.start()
sleep(6)
print('Exam Finished')
'''

'''
def teacher():
    for i in range(1, 11):
        print('Teaching Session : ',i)
        sleep(1)
t1 = Thread(target=teacher)
t1.start()
sleep(6)
t1.join()
print('Exam Finished')
'''


'''
# Using daemon thread
def teacher():
    for i in range(1, 11):
        print('Teaching Session : ',i)
        sleep(1)
t1 = Thread(target=teacher)
t1.daemon = True
t1.start()
sleep(6)
print('Exam Finished')
'''