def An1(x):
    x = (x % 2) * ((3 * x) + 1) + (1 - (x % 2)) * (x / 2)

    return x

def zad19():
    num = None
    maxi = 0
    
    for n in range(2, 10001):
        cnt = 0
        x = n

        while x != 1:
            x = An1(x)
            cnt += 1

        if cnt > maxi:
            num = n
            maxi = cnt

    return num, maxi

print(zad19())
