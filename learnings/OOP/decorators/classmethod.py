class School:
    schoolname = "ABC school"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def changename(cls, name):
        cls.schoolname = name
        return f'This is your new school name: {cls.schoolname})'

    def show(self):
        print(f'{self.name} age is {self.age} and studies in {self.schoolname}')

joey = School('joey', 10)
joey.show()

School.changename("xyz school")
david = School("david", 39)
david.show()
