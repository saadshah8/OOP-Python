# Problem 2: class account with 2 attribute balance & account number, methods for credit, debit, printing current balance
class acc():
    def __init__(self, balance, accnum):
        self.balance = balance
        self.accnum = accnum
        print(f"Account Number: {accnum} | Account Balance: {balance} | CREATED")
    
    def credit(self,credit):
        self.balance += credit
        print(f"{credit} is credited into the account {self.accnum}")
        self.Balance() #calling balance function of same class

    def debit(self,debit):
        self.balance -= debit
        print(f"{debit} is debited from the account {self.accnum}")
        self.Balance() #calling balance function of same class
    
    def Balance(self):
        return(print(f"The current balance is: {self.balance}"))

a1=acc(1000,2016)
a1.credit(500)
a1.debit(800)


