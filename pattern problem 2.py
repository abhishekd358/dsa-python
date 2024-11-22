"""
----*
---***
--*****
-*******
*********
"""
# n = 5
# for i in range(1, n + 2):  
#     underscores = (n + 1 - i) * "_"  
#     stars = (2 * i - 1) * "*"
#     print(underscores + stars)


n = 5
for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()


print("\n+++++++++++++++++++++++++++++++\n")


"""
*********
 *******
  *****
   ***
    *
"""

for i in range(n):
    for k in range(i):
        print(" ", end="")
    for j in range(2*n-((i*2)+1)):
        print("*", end="")    
    print()

print("\n+++++++++++++++++++++++++++++++\n")

"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
n = 5
for i in range(2*n):
 if i<n:
  for j in range(i+1):
   print("*",end = " ")
 else:
  for j in range(i,2*n-1):
   print("*", end = " ")
 print()



"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""
for i in range(n):
    for j in range(i+1):
        if (i+j) % 2==0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()



print("\n+++++++++++++++++++++++++++++++\n")


num = 4
for i in range(num):
    for j in range(i+1):
        print(j+1, end="")

    # for space
    for j in range((num-i-1)*2):
        print(" ", end="")

    for j in range(i+1,0,-1):
        print(j, end="")    
    print()





            