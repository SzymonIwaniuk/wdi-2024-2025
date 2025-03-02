from math import sqrt


def An1(A, B):
    return sqrt(A * B)

def Bn1(A, B):
    return (A + B)/2.0
    

def mean(A, B):
    eps = 1e-10

    while abs(A - B) > eps:
        A, B = An1(A, B), Bn1(A, B)

    return A

print(mean(15, 12))
