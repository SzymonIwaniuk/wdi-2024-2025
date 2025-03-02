from math import log10, sqrt, ceil



def is_prime(n):
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5

    while i <= sqrt(n):
        if n % i == 0: return False

        i += 2
        
        if n % i == 0: return False

        i += 4

    return True


def is_palindrome(n):
    temp = n
    reverse = 0
    
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    
    if n == reverse: return True
    else: return False 
                        


def palindroms_N(N):
    for n in range(1, N):
        temp_n = n

        if is_prime(temp_n) and is_palindrome(temp_n):

            while True:
                lenght = int(log10(temp_n)) + 1
                temp_n = (temp_n % 10 ** (lenght - 1)) // 10

                if not is_prime(temp_n): break
                
        if temp_n == 0: print(n)

print(palindroms_N(100000))

