def fib():
    a, b = 0, 1

    while(b<1000000):
        print(a)
        a, b = b, a + b
        
fib()
