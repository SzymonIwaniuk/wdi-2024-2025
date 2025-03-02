def sumy(t1, t2):
    for i in range(3**len(t1)):
        suma = 0
        c = i
        j = 0
        while j < len(t1):
            if c % 3 == 0:
                suma += t1[j]
            if c % 3 == 1:
                suma += t2[j]
            if c % 3 == 2:
                suma += t1[j] + t2[j]
            c //= 3
            j += 1
        if is_prime(suma):
            print(f"={suma}")
