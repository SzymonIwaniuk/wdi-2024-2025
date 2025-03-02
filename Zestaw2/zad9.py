def fib(a , b):
    return b, a + b

def zad9(n):
    i = n
    flag = n + 1000
     
    while i < flag:
        i += 1
        suma = 0
        a, b = 0, 1
        found = False
        
        while suma < i:
            suma = 0
            a, b = 0, 1
            while suma < i:
                suma +=a
                if suma == i:
                    found = True
                    break
                a, b = fib(a, b)
            if found:
                break
            
            
        if not found:
            return i

    return False 
        
            
print(zad9(17))
