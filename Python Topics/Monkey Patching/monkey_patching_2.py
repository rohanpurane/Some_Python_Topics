from monkey_patching import *




def monkey(amount, status):
    if pay_status == 'Done':
        print('Payment is Done.')
        return print(f"Remaining Balance is {account_balance - payment}")
    elif pay_status == 'Interupt':
        print('Sorry, Payment is Interupted.')
        return print(f"Remaining Balance is {account_balance - payment}, kindly visit your Bank.")
    else:
        print("Oops, Something went wrong...!")

b = Bank()
b.transaction = monkey(payment,pay_status)

