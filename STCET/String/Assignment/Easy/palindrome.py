st=input("Enter String to cheeck for Palindrome:")
l=st[::-1]

if(st==l):
    print("Palindrome")
else:
    print("Not a Palindrome")