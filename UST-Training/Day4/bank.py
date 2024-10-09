class Account:
    def __init__(self, balance =0):
        self.balance = balance

class Savings(Account):
    def __init__(self, name, balance):
        self.name = name
        super().__init__(balance)
    
    def deposit(self, amt):
        if amt > 0: self.balance += amt
        
    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
        else:
            print('Insufficient funds!!')



class Current(Account):
    def __init__(self, name, balance):
        super().__init__(balance)
        self.name = name
    
    def __str__(self) -> str:
        return f'Account holder: {self.name} Current balance: {self.balance}'
    
    def deposit(self, amt):
        if amt > 0: self.balance += amt
        else: print('Enter valid amount to deposit!')
    
    def withdraw(self, amt):
        if self.balance > -1000:
            self.balance -= amt
            print(f'Successfully withdrawn $ {amt}')
        else:
            print('Insufficient funds!!')
    
    def statement(self):
        print(f'Amount Balance: ${self.balance}')

x = Current('UMME', 500)
x.deposit(300)
x.statement()
x.withdraw(1000)
x.statement()
x.withdraw(800)
x.statement()
x.withdraw(1)

print(x)

