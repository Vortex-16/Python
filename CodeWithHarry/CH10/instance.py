class Employee:
    language = "Python"
    salary = 100000

harry = Employee()
harry.name = "Harry" # Dynamically adding an attribute instance
harry.language = "Java" # Dynamically changing the attribute instance
print(harry.name, harry.language, harry.salary) #if not then class attribute will be printed