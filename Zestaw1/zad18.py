#Liczenie pi z ciagu sqrt(0.5) * sqrt(0.5 + 0.5 * a1) * ... = 2/pi

from math import sqrt, pi

def piCiag05() -> float:
    a1 = sqrt(0.5)
    a2 = sqrt(0.5 + 0.5 * a1)
    product = a1 * a2
    eps = 1e-20

    while a2 - a1 > eps:
        a1 = a2
        a2 = sqrt(0.5 + 0.5 * a1)
        product *= a2

    return 2.0 / product

print(piCiag05(), pi)
