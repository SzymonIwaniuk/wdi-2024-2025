import time



def zad13():
    N = 1000000

    for i in range(2, N):
        suma = 1
        j = 2
        while j*j <= i:
            if i % j == 0:
                suma += (j + (i // j))
            j += 1
        if suma == i:
            print(i)
        #end while

    #end for
            
    print("Done")
#start_time = time.time()
#zad13()
#end_time = time.time()
#print(end_time - start_time)


def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def zad14():
    N = 1000000
    p = 2
    print("Perfect numbers up to", N, ":")
    
    # Generate perfect numbers using Euclid-Euler theorem
    while True:
        # Check if (2^p - 1) is prime
        mersenne_prime = 2**p - 1
        if is_prime(mersenne_prime):
            # Calculate the perfect number 2^(p-1) * (2^p - 1)
            perfect_number = 2**(p - 1) * mersenne_prime
            if perfect_number > N:
                break
            print(perfect_number)
        
        p += 1
    
    print("Done")

start_time2 = time.time()
zad14()
end_time2 = time.time()
print(end_time2 - start_time2)
