# Count Digits in a Number
def CountDigit(num):
    number = int(num)
    digits = 0
    while number > 0:
        number = number // 10
        digits += 1
    return digits
    
print(CountDigit(52442))


# Reverse a Number
def ReverseNumber(num):
    ans = 0
    while num > 0:
        rem = num % 10
        ans = ans * 10 + rem
        num = num // 10
    return ans

print(ReverseNumber(1234)) 

# Palindrome 121

def Palindrome(num):
    number = int(num)
    # if reverse is equal to the number then it palindrome
    ans = 0
    while num > 0:
        rem = num % 10
        ans = ans * 10 + rem
        num = num // 10
    if (ans == number):
        return "Yes, It is Palindrome"
    else:
        return "No, It is Not Palindrome"
    
print(Palindrome(121))



# GCD or HCF



#check for Prime

def isPrime(num):

    if num == 2:
        return 'It is a prime'
    if num <= 2:
        return 'Not a prime'
    else:
        if num % 2 == 1:
            return "It is prime"
        else:
            return "Not a Prime"
        
print(isPrime(15))


# method 2
def prime(num):
    if num <2:
        return "No, It's is not Prime"
    for i in range(2, num):
        if num %i == 0:
            return "No, It's is not Prime"
    return "Yes, It's Prime"


""" below is method is used to iterate till the root of given number . and complexity is root of(n)"""

def optimizePrime(num):
    if num <2:
        return "No, It's is not Prime"
    i = 2
    while i*i <=num:
        if num % i == 0:
            return "No, It's is not Prime"
        i+=1
    return "Yes, It's Prime"

print(prime(121))
print(optimizePrime(11))



# print all div

def AllDivisor(num):
    k = 1
    while k*k<= num:
        if num % k == 0:
            print(k)
            if k != (num//k):
                print(num//k)
        k+=1

print(AllDivisor(25))


 
# armstrong

def armstrong(num):
    ans = 0
    temp = num
    # we have to  find len of number for power
    power = len(str(num))  # you can use other method as well
    while num > 0:
        reaminder = num % 10
        num = num // 10
        ans += reaminder**power
    return temp == ans

print(armstrong(123))
print(armstrong(153))


