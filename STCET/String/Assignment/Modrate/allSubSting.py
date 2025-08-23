# Input string
s = input("Enter a string: ")

# List to store all substrings
substrings = []

# Loop through all possible start and end positions
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substrings.append(s[i:j])

# Print all substrings
print("All substrings:", substrings)
