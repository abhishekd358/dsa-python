"""
1 
2 3 
4 5 6
7 8 9 10
11 12 13 14 15
"""
n = 5
x = 1
for i in range(n):
    for j in range(i+1):
        print(x, end=" ")
        x+=1
    print()

print("========================")


"""
A
AB
ABC
ABCD
ABCDE
"""
char_val = 65
for i in range(n):
    for j in range(i+1):
        print(chr(char_val+j), end="")
    print()


print("========================")


"""
ABCDE
ABCD
ABC
AB
A
"""
char_val = 65
for i in range(n):
    for j in range((n-i)):
        print(chr(char_val+j), end="")
    print()


print("========================")


"""
A
BB
CCC
DDDD
EEEEE
"""
char_val = 65
for i in range(n):
    for j in range((i+1)):
        print(chr(char_val+i), end="")
    print()


print("========================")
"""
   A
  ABA
 ABCBA
ABCDCBA
"""
num = 4
char_value = 65
for i in range(num):
    for j in range((num-i)-1):
        print(" ", end="")

    for j in range(i+1):
        print(chr(char_value+j), end="")
    
    for j in range(i, 0, -1): # we reversing the printing
        print(chr(char_value+j-1), end="")

    print()


print("========================")



"""
E
D E
C D E
B C D E
A B C D E
"""
char_val = 65
for i in range(n):
    for j in range(i+1, 0, -1):
        print(chr((char_val+n)-j), end=" ")
    print()