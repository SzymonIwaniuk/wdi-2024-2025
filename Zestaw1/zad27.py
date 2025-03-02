def is_palindrome(n):
    temp = n
    reverse = 0
    
    while temp:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp //= 10
        
    if n == reverse: return True
    else: return False

def binary(n):
    binary = 0

    while n:
        remainder = n % 2
        binary = (binary * 10) + remainder
        n //= 2
        
    return binary

def zad27(n):
    if is_palindrome(n) and is_palindrome(binary(n)): return True 

    return False

print( zad27(33))
        
