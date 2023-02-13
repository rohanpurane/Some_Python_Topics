'''
# This is pattern of Exception Handling
try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass
'''
############################ User Define Exception ############################

'''
n = int(input('Enter number to devide 10 : '))
a = 10
b = n
c = a/b
print(c)

# If n==0 then programe will get terminat by ZeroDivisionError: 
# and our next line code will not execute to tackle this situation
# we need Exception Handling
 
print('Rest of the code')
'''

'''
n = int(input('Enter number to devide 10 : '))

try:
    a = 10
    c = a/n
    
# except Exception:
    # OR
# you can use name of predefine Exception :
except ZeroDivisionError:
    print('You cannot use 0 in this programe...!')
    print()
    if n==0:
        n = int(input("Enter number but don't use 0 again : "))
        c= 10/n
        print(f"The Answer is {c}")
    if n==str:
        print("Don't use Alphabates Use only Numbers")
else:
    print(f"The Answer is {c}")
    print('Congratulations! You have successfully completed Task........!')
finally:
    print('Programe Closed')
'''

'''
n = int(input('Enter number to devide 10 : '))

try:
    a = 10
    c = a/n

except ZeroDivisionError as obj:
    print(obj)
    print()
    if n==0:
        n = int(input("Enter number but don't use 0 again : "))
        c= 10/n
        print(f"The Answer is {c}")
    if n==str:
        print("Don't use Alphabates Use only Numbers")
else:
    print(f"The Answer is {c}")
    print('Congratulations! You have successfully completed Task........!')
finally:
    print('Programe Closed')
'''


'''
# You can use multiple exceptions 
try:
    n = int(input('Enter number to devide 10 : '))
    a = 10
    c = a/n

except ZeroDivisionError as obj:
    print(obj)
    print()
    n = int(input("Enter number but don't use 0 again : "))
    c= 10/n
    print(f"The Answer is {c}")
        
except ValueError:
    print("Can't Use String Use only Numbers...")
    n = int(input("Enter number but don't use 0 again : "))
    c= 10/n
    print(f"The Answer is {c}")
else:
    print(f"The Answer is {c}")
    print('Congratulations! You have successfully completed Task........!')
finally:
    print('Programe Closed')
'''
'''
 
class BalanceException(Exception):
    pass

def bank():
    n = int(input('Enter Amount to Withdraw : '))
    money = 10000
    withdraw =n
    try:
        balance = money-withdraw
        if balance<= 2000:
            raise BalanceException('Insufficient Funds ...!')
        print(balance)
    except BalanceException as be:
        print(be)
bank()
'''


'''
class BankClass():
    def __init__(self, n, money, withdraw):
        self.n = n
        self.money = money
        self.withdraw =withdraw

    def bank(self):  
        self.balance = self.money-self.withdraw
        if self.balance<= 2000:
            raise Exception
        print(self.balance)
n = int(input('Enter Amount to Withdraw : '))
money = 10000
withdraw = n
be = BankClass(n, money, withdraw)
try:
    be.bank()
except Exception:
    print('Insufficient Funds ...!')
else:
    print('Transaction Successfull....!')
finally:
    print(f"Balance Amount is {be.balance}")
'''


############################ Assert Statement ############################

# a = 10
# assert a <= 10     # '10 is less than a'


############################  ############################
