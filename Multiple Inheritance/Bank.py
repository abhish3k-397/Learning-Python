# 6. Create a base class Bank. Derive SavingsAccount and LoanAccount from it. 
#    Then create Customer that inherits from both SavingsAccount and LoanAccount 
#    and manages finances.

class Bank:
    def __init__(self,name):
        self.name = name
class SavingsAccount(Bank):
    def work(self):
        print(f"{self.name} Stores Savings")
class LoanAccount(Bank):
    def work(self):
        print(f"{self.name} Tracks Loans")

class Customer(SavingsAccount,LoanAccount):
    def work(self):
        print(F"{self.name} manges Finance")

SavingsAccount = SavingsAccount("SavingsAccount")
LoanAccount = LoanAccount("LoanAccount")
Customer = Customer("Customer")

LoanAccount.work()
SavingsAccount.work()
Customer.work()
