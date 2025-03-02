def nww(x, y):
    while y:
        x, y = y, x % y
    return x
    

def nwd3(a, b, c):
    while True:
        a, b, c = c % a, a % b, b % c
        
        if a == 0 or b == 0 or c == 0:
            break
    if a > 0 and b > 0:
        result = nwd(a, b)
    elif a > 0 and c > 0:
        result = nwd(a, c)
    else:
        result = nwd(b, c)

    return result

def zad16(a, b, c):

    nww = a * b * c // nwd3(a, b, c)
    return nww

print(zad16(133, 266, 399))
        
