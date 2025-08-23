str=input("Enter a string: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

# Replace the old word with the new word
str = str.replace(old_word, new_word)

print("Updated string:", str)