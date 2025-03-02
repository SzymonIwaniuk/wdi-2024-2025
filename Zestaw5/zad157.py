#Zadanie 157. Tablica T = [(x1, y1), (x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
#wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
#2 niepustych podzbiorów tego zbioru.
from math import sqrt

def midmass(T):
    l = len(T)

    def rek(index,t1,t2):
        if index == l:
            if len(t1) == 0 or len(t2) == 0: return float ('inf')
            if t1 == t2: return float('inf')
            else:
                xs1 = ys1 = xs2 = ys2 = 0
                for i in range(len(t1)):
                    xs1 += t1[i][0]
                    ys1 += t1[i][1]
                xs1, ys1 = xs1 / len(t1), ys1 / len(t1)
                for j in range(len(t2)):
                    xs2 += t2[j][0]
                    ys2 += t2[j][1]
                xs2, ys2 = xs2 / len(t2), ys2 / len(t2)
                return sqrt((xs1-xs2)**2 + (ys1-ys2)**2)

        return min(rek(index + 1,t1 + [T[index]],t2),
                   rek(index + 1,t1,t2 + [T[index]]),
                   rek(index + 1,t1 + [T[index]],t2 + [T[index]]),
                    rek(index + 1, t1,t2))
    return rek(0,[],[])
print(midmass([(1, 2), (7, 8), (3, 4)]))