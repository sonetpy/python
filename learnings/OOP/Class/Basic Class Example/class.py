# https://www.listendata.com/2019/08/python-object-oriented-programming.html
"""
Object :
-------------
Car an object is something that posses some characterstics and can perform function like start, stop, drive and brake.

Function (method):
--------------
like start, stop, drive and brake.

Characterstics (attributes):
----------------
Color, mileage, max speed, model year

How to access a attribute of a Class "Company.name"
"""
class Company:

    # attributes
    name = "HDFC bank"
    turnover = 5000
    revenue = 1000
    no_of_employees = 100

    # method
    def productivity(self):
        return Company.revenue/Company.no_of_employees

c = Company()
print(c.name)
print(c.no_of_employees)
print(c.productivity())


