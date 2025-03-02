def zamien_sys(x, s):
    hexadecimal = '0123456789ABCDEF'
    T = [0 for _ in range(64)]
    i = 0
    
    while x > 0:
        T[i] = x % s
        x //= s
        i += 1

    for i in range(i - 1, -1, -1):
        print(hexadecimal[T[i]], end = "")

    return ""

print(zamien_sys(331,16))





