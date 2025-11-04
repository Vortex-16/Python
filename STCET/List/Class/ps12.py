# Accessing elements in a 2D list
table1=[[1,2,3],[4,5,6]]
print("Value in table1 by row are: ")
for row in table1:
    for itrm in row:
        print(itrm ,end=" ")
    print()