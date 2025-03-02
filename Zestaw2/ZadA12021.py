from math import log10



def cutm(n, c):
    lenght = int(log10(n)) + 1
    
    return n % (10 ** (lenght - c))
        
    
def cutn(n, c):

    while c:
        n //= 10 
        c -= 1
        
    return n

def d_digits(n):
    T = [0 for _ in range(10)]
    
    while n:
        if T[n % 10] > 1: return False 
        T[n % 10] += 1
        n //= 10

    return True 
        

def is_prime(n):
    if n <= 1: return False
    elif n == 2 or n == 3: return True 
    elif n % 2 == 0 or n % 3 == 0: return False

    i = 5

    while i*i <= n:
        if n % i == 0: return False

        i += 2

        if n % i == 0: return False

        i += 4

    return True 

def counter(n):

    cnt = 0
    
    while n:
        cnt += 1
        n //= 10
    return cnt

def main(num):

    result = 0
    lenght = int(log10(num)) + 1
    maxi = 0
    
    for i in range(lenght - 1):
        for j in range(lenght - 1 - i):
            cnt = 0
            temp_num = cutm(cutn(num, j), i)
            
            if is_prime(temp_num) and d_digits(temp_num):
                cnt = counter(temp_num)

            if cnt > result:
                maxi = temp_num

    return maxi 
            
            




print(main(1202742516))
