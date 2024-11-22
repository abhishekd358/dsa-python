
"""
*****
*****
*****
*****
*****
"""

# n = 5
# for i in range(n):
#     print("*****")

"""
*****
*****
*****
*****
*****
"""

# n = 5
# for i in range(n):
#     print("*****")

n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


print("----------------------------------")
""""
*
**
***
****
*****
"""

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()


print("------------------------------------------")  

"""
1
12
123
1234
12345
"""
for i in range(n):
    for j in range(1, i+2):
        print(j, end="")
    print()


print("------------------------------------------")  

"""
1
22
333
4444
55555
"""
for i in range(1, n+1):
    for j in range(i):
        print(i, end="")
    print()

print("------------------------------------------")  

"""
12345
1234
123
12
1
"""
for i in range(n):
    for j in range(1, (n+1)-i):
        print(j, end="")
    print()


print("------------------------------------------")  

"""
*****
****
***
**
*
"""
for i in range(n):
    for j in range(1, (n+1)-i):
        print("*", end="")
    print()


