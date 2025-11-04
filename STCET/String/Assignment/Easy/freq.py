st=input("Enter a string to find freq of each Char: ")
freq={}
for i in st:
    if(i in freq):
        freq[i]+=1
    else:
        freq[i]=1
print("Frequency of each Woed id: ",freq)