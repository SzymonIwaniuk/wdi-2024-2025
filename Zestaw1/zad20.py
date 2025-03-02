def zad20(N):
    result_n = 1e10

    for n in range(2, 10001):
        counter = 0
        x = (n % 2) * ((3 * n) + 1) + (1 - (n % 2)) * (n / 2)

        while x != 1:
            x = (x % 2) * ((3 * x) + 1) + (1 - (x % 2)) * (x / 2)
            counter += 1

        if counter == int(N) and n < result_n:
            result_n = n

    return result_n

print(zad20(99))
