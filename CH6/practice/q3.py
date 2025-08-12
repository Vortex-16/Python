p1="Earn Money" 
p2="Get For Free"
p3="Get it now"
p4="Click This"
msg=input("Enter Your Message: ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("This is a spam message.")
    print("Please refrain from using spammy language.")
else:
    print("This message seems fine.")