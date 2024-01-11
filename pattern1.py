# ****
# *  *
# *  *
# ****
n = 4
for i in range(0, n):
    for j in range(0, n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="") 
        else:
            print(" ", end="")
    print()



# *  *
#  ** 
#  ** 
# *  *
n = 4
for i in range(0, n):
    for j in range(0, n):
        if i == j or i + j == n - 1:
            print("*", end="") 
        else:
            print(" ", end="")
    print()



# * *
#  * 
# * *
n = 3
for i in range(0, n):
    for j in range(0, n):
        if i == j or i + j == n - 1:
            print("*", end="") 
        else:
            print(" ", end="")
    print()



#    *
#   **
#  ***
# ****
n = 4
for i in range(0, n):
    for j in range(0, n):
        if i + j > n / 2:
            print("*", end="") 
        else:
            print(" ", end="")
    print()



 
#     *
#    ***
#   *****
#  *******
n = 4
for i in range(0, n):
    for j in range(0, n - i):
            print(" ", end="")
    for j  in range(0, 2*i + 1):
        print("*", end="")
    print()






