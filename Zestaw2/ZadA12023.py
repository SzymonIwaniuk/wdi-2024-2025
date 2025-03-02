def weryf(a, b):
    d = 2

    while a > 1 and b > 1:
        if a % d == 0 and b % d == 0:
            while a % d == 0:
                a //= d
            while b % d == 0:
                b //= d
        if a % d == 0 or b % d == 0:
            return False
        
        d += 1

    if a > 1 or b > 1:
        return False

    return True

def zgodne(T):
    l = len(T)
    if l < 2:
        return 0
    pom = [0 for _ in range(l)]

    for i in range(l - 2):
        if weryf(T[i], T[i + 1]):
            pom[i] = pom[i+1] = 1
        if weryf(T[i], T[i+2]):
            pom[i] = pom[i+2] = 1

    if weryf(T[-1], T[-2]):
        pom[-1] = pom[-2] = 1

    return sum(pom)

print(zgodne([2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45, 15]))
