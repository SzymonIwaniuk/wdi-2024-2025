def zad12(n):
    i = 5
    while n % 2 == 0:
            print(2)
            n //= 2
    
    while n % 3 == 0:
            print(3)
            n //= 3
    while n != 1:
        while n % i == 0:
            print(i)
            n //= i
        i += 2

        while n % i == 0:
            print(i)
            n //= i
        i += 4
            
        

print(zad12(521479812))
