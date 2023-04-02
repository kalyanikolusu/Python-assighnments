# Challenge 4: Implement a Banking Account
# In this challenge, you will implement a banking account using the concepts of inheritance.
#Problem statement:
#Implement the basic structure of a parent class, Account, and a child class, SavingsAccou
'''class account:
    def __init__(self,title=None,account_balance=0):
        self.title=title
        self.account_balance=account_balance

class savings_account(account):
    def __init__(self,title=None,account_balance=0,inter_rate=0):
        self.inter_rate=inter_rate
        super().__init__(title,account_balance)
# creating an object on child class :
sa1=savings_account("Ashish",5000,5)
print(sa1.title)
print(sa1.account_balance)
print(sa1.inter_rate)'''

# Challenge 5: Handling a Bank Account. In this challenge, you will define methods for handling a bank account using concepts of inheritance.
#Problem statement: In this challenge, we will be extending the previous challenge and implementing methods in the parent class and its corresponding child class.#
#The initializers for both classes have been defined for you.
#Task 1: In the Account class, implement the getBalance() method that returns balance.
#Task2:  In the Account class, implement the deposit(amount) method that adds amount to the balance.

class account:
    def __init__(self,title=None,account_balance=0):
        self.title=title
        self.account_balance=account_balance
    def withdrawal(self,with_amount=500):
        self.with_amount=with_amount
        
    def deposit(self,depo_amount=500):
        self.depo_amount=depo_amount
    def getbalance(self):
        print("The balance amount is : ",self.account_balance-self.with_amount)
ac1=account("ashish",2000)
ac1.withdrawal(500)
ac1.getbalance()
# creating child class :
class savings_account(account):
    def __init__(self,title=None,account_balance=0,inter_rate=0):
        super().__init__(title,account_balance)
        self.inter_rate=inter_rate
    def interestamount(self):
        print("The interestamount is :",(self.account_balance*self.inter_rate)/100)      
# creating object on child class
sa1=savings_account ("Ashish",2000,5)
print(sa1.account_balance)
print(sa1.inter_rate)
sa1.interestamount()
            
