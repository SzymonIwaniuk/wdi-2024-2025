def same_digits(a, b):
    T = [0 for _ in range(10)]
    while a > 0:
        T[a % 10] += 1
        a //= 10

    #end while
        
    while b > 0:
        T[b % 10] -= 1

        if T[b % 10] < 0: return False
        
        b //= 10

    return sum(T) == 0 
    
print(same_digits(1234, 42311))
