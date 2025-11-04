# Write A PYTHON PROGRAM THAT PASSES A LIST TO A FUNCTION THAT SQARES EACH ELEMENT IN THE LIST

def square_elements(input_list):
    return [x ** 2 for x in input_list]

original_list = [1, 2, 3, 4, 5]
squared_list = square_elements(original_list)

print("Original List:", original_list)
print("Squared List:", squared_list)