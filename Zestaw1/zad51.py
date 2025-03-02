from math import sqrt, log10


def is_prime(n):
    if n <= 1: return False
    elif n <= 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False
    else:
        i = 5

        while i <= sqrt(n):
            if n % i == 0: return False

            i += 2

            if n % i == 0: return False

            i += 4

    return True


def bit_mask(n, l):
    binary_digits = [0] * l

    index = l - 1
    while n > 0:
        binary_digits[index] = n % 2
        n //= 2
        index -= 1
    return binary_digits

def check_mask(mask, l1, l2):
    for el in mask:
        if el == 0:
            l1 -= 1
        else:
            l2 -= 1
    return l1 == 0 and l2 == 0

def num_to_tab(n, l):
    tab = [0] * l
    index = l - 1
    n1_tab = num_to_tab(n1,l1)
    n2_tab = num_to_tab(n2,l2)
    while n > 0:
        binary_digits[index] = n % 10
        n //= 10
        index -= 1
    return tab

def zad51(n1,n2):
    l = int(log10(n1)) + 1 + int(log10(n2)) + 1
    
    for i in range(1, 2**l):
        mask = bit_mask(i, l)
        if not check_mask(mask, l1, l2):
            continue

        num = 0
        mul = 1

        n1_index = 0
        n2_index = 0

        for j in range(l):
            if mask[j] == 1:
                num += n2_tab
        











            
