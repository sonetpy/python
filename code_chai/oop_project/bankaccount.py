import random

class Account:
    bank_name = "HDFC Bank"  # 🏦 class attribute (same for all)
    track = 0

    def __init__(self, name, balance):
        self.__name = name       # 👤 instance attribute
        self.__balance = balance # 💰 instance attribute
        self.__account = self.generate_account_number()
        Account.track += 1

    def display(self):
        print(f"{Account.bank_name} welcomes you {self.__name}! "
              f"Account #{self.__account} opened with balance ₹{self.__balance}. "
              f"Total accounts created: {Account.track}")

    def generate_account_number(self):
        # Generate a random 7-digit number (1000000 to 9999999)
        return random.randint(1000000, 9999999)
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self.__balance}")

    @property
    def balance(self):
        """Read-only access to account balance."""
        return f"Balance: ₹{self.__balance}"

    @staticmethod
    def bank_policy():
        return f"Thanks for Banking with {Account.bank_name}"

# ⚡ Derived Class   
class SavingsAccount(Account):   # 👶 Child of Account
    def withdraw(self, amount):
        if amount > 50000:
            print("❌ Withdrawal limit exceeded! (Max ₹50,000 per transaction)")
        else:
            # call parent class withdraw()
            super().withdraw(amount)

# ⚡ Derived Class   
class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount > 10000:
            print(f"❌ Min ₹10,000 should be maintained and current balance: {super().balance}")
        else:
            super().withdraw(amount)

                

# 🧪 Example Usage
person1 = Account("Kumar Abhinav", 18000)
person1.display()
person1.deposit(1200)
person1.withdraw(6000)
print(person1.balance)

person2 = SavingsAccount("Anushka Sharma", 80000)
person2.display()
person2.deposit(1000)
person2.withdraw(2000)

person3 = CurrentAccount("Kiaara", 30000)
person3.display()
person3.deposit(1000)
person3.withdraw(8000)
print(person3.bank_policy())