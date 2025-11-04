import string
s = input("Enter a string: ")


no_punct = "".join(char for char in s if char not in string.punctuation)

print(no_punct)