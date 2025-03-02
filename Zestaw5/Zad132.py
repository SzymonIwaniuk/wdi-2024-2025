
def Newton(n,k):

    def rek(n, k):
        if k == 1:
            return n
        if n == k:
            return 1

        return rek(n - 1, k - 1) + rek(n - 1, k)

    result = rek(n, k)
    return result

print(Newton(20,10))