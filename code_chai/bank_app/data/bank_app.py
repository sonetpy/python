import random

class Account:
    bank_name = "HDFC Bank"  # 🏦 class attribute (same for all)
    track = 0
    accounts = {}  # 🧾 store transaction history
    def __init__(self, name, balance):
        self.__name = name       # 👤 instance attribute
        self.__balance = balance # 💰 instance attribute
        self.__account = self.generate_account_number()
        Account.track += 1
        Account.accounts[self.__account] = self

    def display(self):
        print(f"{Account.bank_name} welcomes you {self.__name}! "
              f"Account #{self.__account} opened with balance ₹{self.__balance}. "
              f"Total accounts created: {Account.track}")
    
    def get_account_number(self):
        """🔒 Read-only access to private account number."""
        return self.__account

    def generate_account_number(self):
        # Generate a random 7-digit number (1000000 to 9999999)
        return random.randint(1000000, 9999999)
    
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
        else:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self.__balance}")
    
    
    @property
    def show_transaction(self):
        return Account.accounts

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


while True:
    print("\n===== 🏦 HDFC Mini Bank =====")
    print("1️⃣ Open Account")
    print("2️⃣ Deposit")
    print("3️⃣ Withdraw")
    print("4️⃣ Check Balance")
    print("5️⃣ Show Transactions")
    print("6️⃣ Exit")
    
    choice = input("Enter choice: ").strip()

    if choice == "1":
        # ask user which type: Savings / Current
        # create object and store in dict {account_number: object}
        type_of_account = input("Enter account type (savings/current): ").strip().lower()
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        person = Account(name, initial_deposit)
    elif choice == "2":
        # find account by number, call deposit()
        pass
    elif choice == "3":
        # find account by number, call withdraw()
        pass
    elif choice == "4":
        # print balance using @property
        pass
    elif choice == "5":
        # show transaction history
        for acc_num, account in person.show_transaction.items():
            print(f"Account #{acc_num}: Name: {person.Account__name}, "
                      f"Balance: ₹{acc._Account__balance}, "
                      f"Type: {'Savings' if isinstance(acc, SavingsAccount) else 'Current' if isinstance(acc, CurrentAccount) else 'Account'}"))
    elif choice == "6":
        print("👋 Thanks for using HDFC Mini Bank")
    else:
        print("❌ Invalid option")


