# Take input from user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

# Check if substring exists
if substring in main_string:
    print("Substring exists!")
else:
    print("Substring does not exist.")
