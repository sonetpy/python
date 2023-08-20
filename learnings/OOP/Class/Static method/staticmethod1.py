"""
Python has three types of methods (normal, class, and static).
It's confusing and sometimes we're wondering why do we need all of them.
Even, there are people saying we do not need static method at all and recommend not using it.

The normal and class method requires passing in the first argument:
self for normal method
cls for class method
but a static method requires none to be passed
"""
class Employee(object):
 
    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name
 
    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement
 
    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)
 
emp = Employee('Kelly', 12000, 'ABC Project')
emp.work()