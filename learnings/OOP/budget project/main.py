from expBudget import Budget

def main():
    money=input("Enter the money to spend: $")
    expense = Budget(money)

    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display Balance
        2. Request for Clothing
        3. Request for Samosa
        4. Request for entertainment
        5. Request Expense Summary  
        6. exit
        """)

        choice = int(input("Enter choice: "))
        if choice == 1:
            expense.total()
        elif choice == 2:
            num_cloth=int(input("Enter a number of cloth you want: "))
            expense.clothing(num_cloth)
        elif choice == 3:
            samosa=int(input("Enter number of samosa you want: "))
            expense.food(samosa)
        elif choice == 4:
            ent=int(input("Enter number of entertainment tickets you want: "))
            expense.entertainmnet(ent)
        elif choice == 5:
            expense.summary()
        else :
            expense.exitapp()
    print("Thank you for using the Expense system.")

if __name__ == '__main__':
    main()