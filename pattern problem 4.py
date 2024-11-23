"""
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
"""



n = 5
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")

    for j in range((i*2)):
        print(" ", end= " ")

    for j in range(n-i):
        print("*", end=" ")
    print()

for k in range(n):
    for l in range(k+1):
        print("*", end=" ")
    
    for l in range(n*2-((k+1)*2)):
        print(" ", end=" ")
    
    for l in range(k+1):
        print("*", end=" ")
    print()

print("\n+++++++++++++++++++++++++++++++++++++++++\n")

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")

    for j in range(n*2-((i+1)*2)):
        print(" ", end=" ")
    
    for j in range(i+1):
        print("*", end=" ")
    
    print()

for x in range(n):
    for y in range(n-x-1):
        print("*", end=" ")

    for y in range((x+1)*2):
        print(" ", end=" ")

    for y in range(n-x-1):
        print("*", end=" ")

    print()


print("\n+++++++++++++++++++++++++++++++++++++++++\n")


num = 2
for i in range(num):
    for j in range(i):
        print("*", end="")



