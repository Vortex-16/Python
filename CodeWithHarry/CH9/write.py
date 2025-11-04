st = "This is a sample text. This is amazing"
f = open("E:/Python/CodeWithHarry/CH9/sample.txt", "w")
f.write(st)
f.close()
print("File written successfully.")
f = open("E:/Python/CodeWithHarry/CH9/sample.txt", "r")
print(f.read())
f.close()
#appending
f = open("E:/Python/CodeWithHarry/CH9/sample.txt", "a")
f.write(" This is appended text.")
f.close()
#multiLine
f = open("E:/Python/CodeWithHarry/CH9/more.txt", "r")
print(f.read())
print(type(f))
f.close()

with open("E:/Python/CodeWithHarry/CH9/more.txt") as f:
    print(f.read())
    print(type(f))

#you can also use with statement(without close)