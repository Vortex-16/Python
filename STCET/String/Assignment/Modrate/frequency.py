# Input
sentence = input("Enter a sentence: ")

# Split into words
words = sentence.split()

# Dictionary to store frequency
freq = {}

# Count each word
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Print frequencies
for word, count in freq.items():
    print(word, ":", count)
