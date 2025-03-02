from math import log10

def isPrime(n):
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5

    while i*i <= n:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4

    return True

def devide(N):
    reverse = 0
    while N > 0:
        digit = N % 10
        reverse = reverse * 10 + digit
        N //= 10
    def rek(reverse,t):

        if reverse == 0:
            if isPrime(len(t)):
                for n in t:
                    if not isPrime(n): return False
                return True
            else:
                return False

        digit = reverse % 10
        t1 = t + [digit]
        if t:
            t2 = t[:]
            t2[-1]= t2[-1] * 10 + digit
            if isPrime(t2[-1]):
                return rek(reverse // 10, t1) or rek(reverse // 10, t2)
            else:
                return rek(reverse // 10, t1)

        else:
            return rek(reverse // 10, t1)


    return rek(reverse,[])

print(devide(2222))