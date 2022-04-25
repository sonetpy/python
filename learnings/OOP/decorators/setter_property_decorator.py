class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{self.fname}.{self.lname}@python.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return "email is not set please set it using setter"
        return f"{self.fname}.{self.lname}@python.com"
# suppose I want to take email this.that@indian.com seperate the names with firstname and lastname
    @email.setter
    def email(self, string):
        print("setting now")
        names = string.split("@")[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]
        print(f"Yahi naam hai bhai ka dude : fisrtname = {self.fname} and lastname = {self.lname}")

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani = Employee('hindustani', 'supporter')
#nepali = Employee('nepali', 'babu')
print(hindustani.explain())
# Commented below because I commented the self.email
#print(hindustani.email)
#print(nepali.explain())
# after adding setter or deleter
print(hindustani.email)
print("Now hidustani went to US and he wants to change is fname")
## What do you think this will change the fname to american .. Answer is NO
hindustani.fname = "american"
# Commented below because I commented the self.email
#print(hindustani.email)
# added @property on email (self) method, so commenting below
#print(hindustani.email())
print(hindustani.email)
hindustani.email = "this.that@python.com"
print(hindustani.email)

del hindustani.email
print(hindustani.email)