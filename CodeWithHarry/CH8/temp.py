def temp(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def temp2(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(temp(37))
print(temp2(98.6))