from math import *

def binary(a):
    num = 0
    i = 0
    
    while a >= 1:
        rest = a % 2
        a //= 2
        num += rest * 10**i
        i += 1
        
    return num


def palindrome(n):
    num = binary(a=n)
    lenght = int(log10(num) + 1)
    even = "flag" 
    remainder1 = num
    remainder2 = num
     

    for i in range(1 , lenght + 1):
        if remainder1 % 10 == remainder2 // 10**(lenght - i):
            remainder1 //= 10
            remainder2 -= 10**(lenght - i) * (remainder2 // 10**(lenght - i))
        else:
            return False
    return True
        
    
print(palindrome(13))
#print(binary(10))
