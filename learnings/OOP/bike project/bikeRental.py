# https://www.youtube.com/watch?v=rkgm4uIUnOI
class bikeShop:

    def __init__(self,stock=0):
        self.stock = stock

    def displayBike(self):
        print(f"Bikes Available in stocks: {self.stock}")

    def rentBike(self,number=0):
        self.number = number
        print(f"Total amount for {self.number} bikes is ${self.number * 10}")
        print(f"Total Bikes Available: {self.stock - self.number}")

    def ReturnBike(self,bikereturn):
        self.bikereturn = bikereturn
        print(f"Number of bike returned: {self.bikereturn}")
        print(f"Total bike in stock is now: {self.stock - self.number + self.bikereturn}")

    def exitShop(self):
        exit ()