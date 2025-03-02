from math import log10

def netwon(n):
    
    for i in range(1, 10**n + 1):
        total = 0
        num = i
        l = int(log10(i)) + 1
                
        while num > 0:
            digit = num % 10
            total += digit**l
            num //= 10

        if i == total:
            print(i)
netwon(10)
    
