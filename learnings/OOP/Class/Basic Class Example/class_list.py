class Customer:
    def __init__(self,name,membership):
        self.name = name
        self.membership = membership

customers=[Customer("Sachin", "Platinum"), Customer("Virat", "Platinum")]
for i in range(len(customers)):
    print(customers[i].name)