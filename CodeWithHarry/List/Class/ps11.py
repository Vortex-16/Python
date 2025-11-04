# # Creating a histogram
# value=[]
# print("Enter 10 integers ")
# #taking 10 inputs
# for i in range (10):
#     newValue=int(input((i+1)))
#     value+=[newValue]
#     #Creating histogram
# print("\nCreating a hsitogram from values")
# print("%s%15s%19s"%("Element ","Value ","Histogram"))
# for i in range(len(value)):
#     print("%7d%15s%11s"%(i,value[i] , "*"*value[i]))

# Creating a histogram
values = []
print("Enter 10 integers:")

# Taking 10 inputs
for i in range(10):
    new_value = int(input(f"Enter value {i+1}: "))
    values.append(new_value)

# Creating histogram
print("\nCreating a histogram from values")
print(f"{'Element':>7} {'Value':>10} {'Histogram'}")
for i, val in enumerate(values):
    print(f"{i:7d} {val:10d} {'*' * val}")