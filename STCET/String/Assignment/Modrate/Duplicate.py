# Take input
string = input("Enter a string: ")

# Initialize an empty string to store result
result = ""

# Loop through each character
for char in string:
    if char not in result:
        result += char  # add only if not already in result

print("String after removing duplicates:", result)
