payment = int(input("Enter Amount to make Payment : "))
pay_status = input("Enter Payment Status (Done or Interupt) : ")
account_balance = 10000
class Bank():
    
    def transaction(self,amount, status):
        if pay_status == 'Done':
            print('Payment is Done.')
            return print(f"Remaining Balance is {account_balance - payment}")

        elif pay_status == 'Interupt':
            print('Sorry, Payment is Interupted.')
            return print(f"Your Account Balance is reamin same {account_balance}, kindly try again.")
        else:
            print("Oops, Something went wrong...!")



