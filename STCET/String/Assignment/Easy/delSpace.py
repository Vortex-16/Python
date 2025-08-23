st=input("Enter a string to remove all space: ")
stList=st.split(" ")
newSt=""
for i in stList:
    newSt+=i
print(newSt)