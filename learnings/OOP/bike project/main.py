from bikeRental import bikeShop

def main():
    bike_quantity=int(input("Enter the quantity of bike you have in stock: "))
    shop = bikeShop(bike_quantity)

    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on rent $10
        3. Return a bike
        4. Exit
        """)

        choice = int(input("Enter choice: "))
        if choice == 1:
            shop.displayBike()
        elif choice == 2:
            numberofbike=int(input("Enter a number of bike you want to rent: "))
            shop.rentBike(numberofbike)
        elif choice == 3:
            returnbike=int(input("Enter number of Bike you want to return: "))
            shop.ReturnBike(returnbike)
        else:
            shop.exitShop()
    print("Thank you for using the bike rental system.")

if __name__ == '__main__':
    main()