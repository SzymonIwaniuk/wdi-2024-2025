from math import sqrt

def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False
    if n == 3:
        return True  # 3 is a prime number
    if n % 3 == 0:
        return False

    limit = int(sqrt(n)) + 1
    x = 5
    while x <= limit:
        if n % x == 0 or n % (x + 2) == 0:
            return False
        x += 2  # Increment by 2 first
        if x <= limit and n % x == 0:
            return False
        x += 4  # Then increment by 5

    return True

print(isprime(121))  # Should print False
print(isprime(29))   # Should print True
