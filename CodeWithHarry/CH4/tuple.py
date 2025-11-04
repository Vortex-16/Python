a = (6, 9, "hello", 3.14, True, None)
# a[0] = 10  
# This will raise an error because tuples are immutable
print(type(a))
i = a.index("hello")
print(i)
print("hello" in a)