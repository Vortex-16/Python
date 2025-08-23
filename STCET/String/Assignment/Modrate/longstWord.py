str=input("Enter a string: ")
words = str.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)
