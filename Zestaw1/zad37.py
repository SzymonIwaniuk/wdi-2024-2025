def zad37(*args):
    t = tuple(args)
    a0 = 0
    a1 = 1
    b0 = 2
    an = a1 - b0 * a0
    bn = b0 + 2 * a0
    for i in t:
        if i == a0: print(b0)
        a0, a1, an, b0, bn = a1, an, an - bn * a1, bn, bn + 2 * a1


zad37(0, 1, 1)
        
        
        
