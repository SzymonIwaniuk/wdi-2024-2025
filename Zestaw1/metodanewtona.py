def newton_sqrt(n, eps = 1e-10):

    x = n / 2

    while True:
        next_x = x - (x ** 2 - n)/(2*x)

        if abs(next_x -x) < eps:
            break

        x = next_x


    return x


print(newton_sqrt(20))
    
