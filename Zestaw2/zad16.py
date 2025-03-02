from math import floor, log10

# Function to calculate the sum of the digits of a number
def digitsum(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

# Function to calculate the sum of the prime factors of a number
def factors_sum(n):
    x = 2
    sum_factors = 0
    while n > 1:  # Fix: should be n > 1, not n >= 1
        if n % x == 0:
            sum_factors += digitsum(x)  # Add the digits of the prime factor
            n //= x  # Reduce n
        else:
            x += 1
    return sum_factors

# Prime number check to exclude primes from being Smith numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find and print Smith numbers
def isSmith():
    i = 1
    while i < 100:
        if not is_prime(i) and digitsum(i) == factors_sum(i):
            print(i)
        i += 1  # Increment i!

isSmith()
