#Volatile = RAM
#Non-Volatile= ROM (SSD | HDD)
'''
File handling in Python
'''
# Use forward slashes which work in all operating systems
f = open("e:/Python/CodeWithHarry/CH9/file.txt")
data = f.read()
print(data)
f.close()   