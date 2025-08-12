a=int(input("Enter a number: "))
b=int(input("Enter Second number: "))
c=int(input("Enter Third number: "))
d=int(input("Enter Fourth number: "))

if(a>b and a>c and a>d):
    print("A is the largest number")
elif(b>a and b>c and b>d):
    print("B is the largest number")
elif(c>a and c>b and c>d):
    print("C is the largest number")
else:
    print("D is the largest number")