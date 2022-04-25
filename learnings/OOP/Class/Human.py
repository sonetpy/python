class Human:
    def __init__(self, name, occ):
        self.name = name
        self.occupation = occ
    def do_work(self):
        if self.occupation == "Cricketer":
            print(self.name, " plays Cricket")
        elif self.occupation == "actor":
            print(self.name, " Shot film")
    def speaks(self):
        print(self.name, "says how are you?")

sachin = Human("Sachin", "Cricketer")
sachin.do_work()
sachin.speaks()
tom = Human("Tom", "actor")
tom.do_work()
tom.speaks()

print("\nAnother way of coding without creating object just by calling Class itself")

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def Print(self):
        print (f"Emplayee Name: {self.name} \nEmployee Id: {self.id}")
        
Employee('bhootnath ji', 5).Print()
#OR
e=Employee('tom bhai', '6')
e.Print()

