class Account(object):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


a1 = Account(0)
a2 = Account(300)

a1.deposit(100)
a2.deposit(40)
a2.deposit(400)
print("Balance is", a1.get_balance())
print("Balance is ", a2.get_balance())

#refrence Copy
a3 = Account(0)
a4 = a3
a4.deposit(100)
print("Balance is", a3.get_balance())
