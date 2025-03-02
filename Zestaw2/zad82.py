def pierwiastek(n):
    x0 = 2
    xk = (x0 + (2 / x0)) / 2
    
    a = [0 for i in range(n + 1)]

    while a[n] == 0:
        tmp = xk
        i = 0
        
        for i in range(n + 1): 
            a[i] = int(tmp % 10)
            tmp -= tmp % 10
            tmp *= 10
             
        x0, xk = xk, (x0 + (2 / x0)) / 2 
        

    print(a[n])

pierwiastek(15)
