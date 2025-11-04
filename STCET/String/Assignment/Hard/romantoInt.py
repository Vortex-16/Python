def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for c in s[::-1]:
        if roman[c] < prev:
            total -= roman[c]
        else:
            total += roman[c]
        prev = roman[c]
    return total

print(roman_to_int("MCMXCIV"))  # 1994
