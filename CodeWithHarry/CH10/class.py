class Employee:
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary

harry = Employee("Harry", "Python", 100000)
print(harry.name, harry.language, harry.salary)
#This will give an error as we have not provided the arguments while creating the object of the class.