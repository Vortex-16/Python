sub1=int(input("Enter Msrks Of First Subject: "))
sub2=int(input("Enter Msrks Of Second Subject: "))
sub3=int(input("Enter Msrks Of Third Subject: "))
totalper=(sub1+sub2+sub3)/3
if((sub1>=33)and(sub2>=33)and(sub3>=33) and (totalper>=40)):
    print("You are promoted to next class.")
else:
    print("You are not promoted to next class.")