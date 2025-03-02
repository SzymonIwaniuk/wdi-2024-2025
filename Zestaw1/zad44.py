from math import log10, sqrt

def is_prime(n):
    if n <= 1: return False
    elif n <= 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False
    else:
        i = 5

        while i <= sqrt(n):
            if n % i == 0: return False

            i += 2

            if n % i == 0: return False

            i += 4

    return True

def is_palindrome(n):
    reverse = 0
    temp = n

    while temp:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if reverse == n:
        return True

    return False
    
def sup_palindroms(n):

    for p in range(1, n):
        temp = p
        lenght_p = int(log10(p)) + 1
        middle_zero = (p // (10 ** (lenght_p // 2 ))) % 10 
        if is_prime(p) and is_palindrome(p) and middle_zero != 0:

            while temp:
                digit = temp % 10
                lenght = int(log10(temp)) + 1
                
                if digit == 0:
                    while temp % 10 == 0:
                        temp //= 10

                else:
                    temp = (temp - digit * 10 ** (lenght - 1)) // 10

                if temp == 0:
                    print(p)
                    
                if not is_prime(temp): break

print(sup_palindroms(100000))
        




                
        
