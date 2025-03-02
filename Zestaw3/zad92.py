def spirala(T):
    N = len(T)
    l = 1 ; b = 0 ; e = N - 1

    while b <= e:
        for k in range(b, e + 1):
            T[b][k] = l
            l = l + 1
        for w in range(b + 1, e):
            T[w][e] = l
            l = l + 1
        for k in range(e, b,- 1):
            T[e][k] = l
            l = l + 1
        for w in range(e, b, - 1):
            T[w][b] = l
            l = l + 1
        b = b + 1
        e = e - 1
    return T

T =  [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]

print(spirala(T))
