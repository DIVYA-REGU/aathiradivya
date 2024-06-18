class Account:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,deposit):
        print("ACCOUNT NUMBER : ",self.account_number)
        print("BALANCE : ",self.balance)
        self.deposit=deposit
        print("deposited amount : ",self.deposit)
        print("new balance : ",self.balance+self.deposit)
    def withdraw(self,withdraw):
        print("ACCOUNT NUMBER : ",self.account_number)
        print("BALANCE : ",self.balance)
        self.withdraw=withdraw
        print("enter the amount to be withdrawn : ",self.withdraw)
        if self.withdraw>self.balance:
            print("insufficient balance")
        else:
            print("new balance after withdrawn :  ",self.balance-self.withdraw)
person1=Account(12345,1200000)
person1.deposit(500)
person1.withdraw(10000)
        
