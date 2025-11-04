class Employee:
    def __init__(self, name, language, salary): #tender 
        self.name = name
        self.language = language
        self.salary = salary
    def greet(self):
        return "Hello, World!"
    @property
    def name(self):
        return self._name
harry = Employee("Harry", "Python", 100000)
print(harry.name, harry.language, harry.salary)
harry.name = "CodeWithHarry"
print(harry.name, harry.language, harry.salary)
print(harry.greet())