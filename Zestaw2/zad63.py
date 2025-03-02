def e_approx(size):
    e = [0 for _ in range(size)]
    a = [0 for _ in range(size)]

    e[0] = 1
    a[0] = 1
    n = 1
    b = True
    
    while b:
        p = 0
        b = False
        for i in range(size - 1, -1, -1):
            s = e[i] + a[i] + p
            e[i] = s % 10
            p = s // 10

        n += 1
        r = 0
        
        for j in range(size):
            t = ((r * 10) + a[j])
            a[j] = t // n

            if a[j] > 0 : b = True
            
            r = t % n
    print(e[0], end = ",")

    for d in e[1:]:
        print(d, end = "")
        
    
e_approx(200)
