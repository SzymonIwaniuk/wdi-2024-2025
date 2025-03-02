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


def zad46(T):
    L = T[0]
    U = T[1]

    for i in range(L, U + 1):
        temp = i
        new_temp = 0
        
        while is_prime(i):
            
            while temp != 0:
                new_temp += (temp % 10) ** 2
                temp //= 10

            if new_temp == 1:
                print(i)
                break
            elif new_temp == 4:
                break

            temp, new_temp = new_temp, 0


print(zad46([1, 100000]))
