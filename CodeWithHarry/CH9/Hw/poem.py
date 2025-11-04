f=open("CodeWithHarry/CH9/Hw/poem.txt")
c=f.read()
if("Papa" in c):
    print("Found 'Papa' in the poem.")
print(c)
f.close()