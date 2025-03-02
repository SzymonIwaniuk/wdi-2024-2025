from math import sqrt




def zad1():
    N = int( input() )
    for a in range(1, N):
        for b in range(1, N):
            if a**2 + b**2 < N**2:
                print(a , b , sqrt(a**2 + b**2))
        #end for
    #end for

zad1()


