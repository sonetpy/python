class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Employee: {self.name}\nId: {self.id}")

    def airlines(self):
        airlines = input("enter new airlines")
        print("new airlines", airlines)
