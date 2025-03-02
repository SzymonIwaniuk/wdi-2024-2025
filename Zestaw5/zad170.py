#Zadanie 170. Dana jest funkcja Ackermana, określona na zbiorze liczb całkowitych nieujemnych, dana
#wzorem rekurencyjnym:

def f(a,b):
    if a==0: return b+1
    if b==0: return f(a-1,1)
    return f(a-1, f(a,b-1))

#print(f(3,7))


def ackermann_iterative(m, n):
    stack = [m]  # Stos do przechowywania wartości m

    while stack:
        m = stack.pop()
        if m == 0:
            n += 1
        elif n == 0:
            n = 1
            stack.append(m - 1)
        else:
            stack.append(m - 1)
            stack.append(m)
            n -= 1

    return n


# Przykładowe wywołanie
print(ackermann_iterative(3, 4))  # Daje wynik 125
