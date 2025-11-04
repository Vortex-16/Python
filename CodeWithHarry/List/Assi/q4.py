#Create a lit of string write a python program which create another list from the frist taking the fisrt taking the first charcter from each word



words = ["apple", "banana", "cherry", "date", "elderberry"]

# Create a new list with the first character of each word
first_chars = [word[0] for word in words]
print(first_chars)