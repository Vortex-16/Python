# Input
s = input("Enter a string: ")

# Dictionary to count frequency of each character
freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Find first non-repeated character
for char in s:
    if freq[char] == 1:
        print("First non-repeated character is:", char)
        break
else:
    print("No non-repeated character found.")
