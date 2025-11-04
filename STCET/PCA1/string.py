s=input("Enter a string: ")
#rev by char

rev = s[::-1]
print(rev)   


#rev by word
rev = " ".join(reversed(s.split()))
print(rev)   