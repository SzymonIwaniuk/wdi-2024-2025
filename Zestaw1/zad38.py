def zad38(*args):
    tup = tuple(args)
    N = len(tup)
    
    for i in range(2, N - 3):
        element = tup[i]
        suma = 0
        for j in range(i - 2, i + 3):
            suma += tup[j]

        if suma / 5 == element:
            print(tup[i])
            


print(zad38(2, 3, 2, 7, 1, 2, 4, 8, 5, 2, 2, 9, 9, 9, 9, 9, 0))

        
            
        
    
    
