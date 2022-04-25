"""
“Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories”
"""
class Budget:
    money = 0

    def __init__(self,balance):
        self.balance = balance
        Budget.money = Budget.money + int(self.balance)
        self.initial_amount = Budget.money
        self.total_clothing=0
        self.total_samosa=0
        self.total_ent=0
        self.amount_left=0

    def total(self):
        print(f"Money you have ${Budget.money}")

    def clothing(self,items=0):
        self.items = items
        self.total_clothing = self.items * 10
        print(f"Money wasted on Cloth: ${self.total_clothing}")
        if self.total_clothing > Budget.money:
            print("You are out of funds dude!")
            self.summary()
            exit()
        else:
            Budget.money = Budget.money - self.total_clothing
            print(f"You are left with ${Budget.money}")

    def food(self,samosa=0):
        self.samosa = samosa
        self.total_samosa = self.samosa * 10
        print(f"You were Hungry and spent ${self.total_samosa}")
        if self.total_samosa > Budget.money:
            print("You are out of funds dude!")
            self.summary()
            exit()
        else:
            Budget.money = Budget.money - self.total_samosa
            print(f"You are left with ${Budget.money}")


    def entertainmnet(self,ent=0):
        self.ent = ent
        self.total_ent = self.ent * 10
        print(f"Wasted on Entertainment ${self.total_ent}")
        if self.total_ent > Budget.money:
            print("You are out of funds dude!")
            self.summary()
            exit()
        else:
            Budget.money = Budget.money - self.total_ent
            print(f"You are left with ${Budget.money}")
        

    def summary(self):
        self.ts = str(self.total_samosa/self.initial_amount * 100)
        self.tc = str(self.total_clothing/self.initial_amount * 100)
        self.te = str(self.total_ent/self.initial_amount * 100)
        print(f"Spent on Cloth {self.tc}%")
        print(f"Spent on Food {self.ts}%")
        print(f"Spent on Entertainment {self.te}%")

    def exitapp(self):
        exit ()
        
