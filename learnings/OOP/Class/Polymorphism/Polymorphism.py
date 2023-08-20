# Similarly, the same method name can be defined in different classes and subclasses, and the appropriate one will be called depending on the object that invokes it
class Person(object):
    def eat(self): print("Person - Eat")

    def drink(self): print("Person - Drink")

    def sleep(self): print("Person - sleep")


class Employee(Person):
    def eat(self): print("Employee - Eat")

    def drink(self): print("Employee - Drink")

    def sleep(self): print("Employee - sleep")


class SalesPerson(Employee):
    def eat(self): print("Salesperson - Eat")

    def drink(self): print("Salesperson - Drink")

    def sleep(self): print("Salesperson - sleep")


def night_out(xyz):
    xyz.drink()
    xyz.eat()
    xyz.sleep()


def main():
    p = Person()
    e = Employee()
    s = SalesPerson()
    night_out(p)
    night_out(e)
    night_out(s)


if __name__ == '__main__':
    main()
