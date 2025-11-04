# *
# * *
# * * *

for i in range(1, 5):
    print("* " * i)

print()







#      *
#     * *
#    * * *
for i in range(1, 5):
    print(" " * (5 - i) + "* " * i)






# * * *
#  * *
#   *
n = 5
for i in range(n):
    print(" " * i + "* " * (n - i))

print()






#      *
#     * *
#    * * *
#     * *
#      *

# Diamond Pattern
n = 3

# Top half
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

# Bottom half
for i in range(1, n):
    print(" " * i + "*" * (2*(n-i)-1))

print()








#    *
#  * *
# * * *

for i in range(1, 6):
    print(" " * (n-i) + "*" * i)

print()




# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

n = 5
for i in range(n):
    print(" " * i + "*" * (n - i))
print()