st=input("Enter a string to cheek for vowel: ")
c=0
l=len(st)
for i in st:
    if i in ['a','e','i','o','u']:
        c+=1
print("Vowel Count is: ",c)