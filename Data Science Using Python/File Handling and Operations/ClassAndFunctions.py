### Step 1: Create class and required functions

class Bank_Account:
#The _init_ function run as soon as an object of a class is instantiated
    def __init__(self):
        self.balance=0
        print("Hello! Welcome to the Deposit & Withdrawal Machine")
#function to deposit money
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
#function to withdraw money
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
#function to display the amount
    def display(self):
        print("\n Net Available Balance=",round(self.balance,2) )


### Step 2: Create object of the class and call the functions

# create object of the class
s = Bank_Account()

# Call functions with that class object
s.deposit()
withdraw_amt = float(input("Enter amount to withdraw: "))
# Pass arguement to the withdraw function
s.withdraw(withdraw_amt)
s.display()

