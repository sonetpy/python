"""
              Robbers (Class)
              1) the professor (derived class)
              2) Band_of_robbers (derived class)

The key points that we can infer are:

* Here, we have 2 subclasses Professor and Band_Of_Robbers that inherit the attributes and methods of the base class Robbers. In addition, they also have their own attributes and methods

* A child class is simply a specialization of the parent class

* Both Professor and Band_Of_Robbers override a parent method Personality and create their own version. You can override any method, including __init__(). This is method overriding

*The class Band_Of_Robbers has a method called family, which is not present in its parent class Robbers
You can add or override a method from the parent. What if you want to call the parent version of that method? In such case super() comes to your aid

* The super() gets the definition of class Pet, parent class
The __init__() method automatically takes care of passing the self argument to the superclass. All you need is to give optional arguments if any

* In the class Band_Of_Robbers, the line self.weapon = weapon and the instance method family is the new code that makes class Band_Of_Robbers different from a Robbers

So, inheritance supports code reusability, by allowing you to create a generic parent class and a more specific child class, which automatically gains access to functionalities of the parent class.

"""
import datetime
from datetime import date

class Robbers:
  def __init__(self, name, alias, gender, bdate):
    self.name = name
    self.alias = alias
    self.gender = gender
    self.bdate = bdate
 
  def personality(self):
       print("I am one of the Money Heist character")
 
  def calculateAge(self, bdate):
    today = date.today()
    age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
    return age

class Professor(Robbers):
    def __init__(self, name, alias, gender, bdate, role):
       super().__init__(name, alias, gender, bdate)
       self.name = name + '"' + " aka " + self.alias + '"'
       self.role = "The master mind of the heist"

    def personality(self):
       print(self.alias, "is an enigmatic charcter, sophisticated but nerdy, charismatic yet shy villain")
 
class Band_Of_Robbers(Robbers):
   def __init__(self, name, alias, gender, bdate, role, weapon):
       super().__init__(name, alias, gender, bdate)
       self.role = role
       self.weapon = weapon
 
   def family(self, related_to):
       return related_to

   def personality(self, i):
     switcher={
                'tokyo':"Tokyo is a strong female lead and a free soul",
                'berlin':"Berlin can be considered cold, hypnotic, sophisticated with high observational skills",
                'nairobi': "A level-headed female focused accomplishing the job"
             }
     return switcher.get(i,"Invalid character")
 
Berlin = Robbers('Andrés de Fonollosa', 'Berlin', 'Male', '1978-07-08')
print("Character:", Berlin.name, "\nAlias:", Berlin.alias)
Berlin.personality()
 
Professor = Professor('Sergio Marquina', 'The Professor', 'Male', '1980-07-08', '')
dob = datetime.datetime.strptime(Professor.bdate, '%Y-%m-%d')
print("\nCharacter:", Professor.name, "\nAlias:", Professor.alias, "\nAge:", Professor.calculateAge(dob),"\nRole:", Professor.role)
Professor.personality()
 
Tokyo = Band_Of_Robbers('Silene Oliveira', 'Tokyo', 'Female', '1990-07-08', 'Robber', 'Heckler & Koch MP5')
dob = datetime.datetime.strptime(Professor.bdate, '%Y-%m-%d')
print("\nCharacter:", Tokyo.name, "\nAlias:", Tokyo.alias, "\nAge:", Tokyo.calculateAge(dob),"\nRole:", Tokyo.role, "\nWeapon:", Tokyo.weapon)
Tokyo.personality('tokyo')
print("Related to:", Tokyo.family('Rio'))
