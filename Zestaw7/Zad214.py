# Zestaw 7: Struktury drzewiaste
# Zadanie 214. Proszę napisać następujące funkcje:
# 1. Funkcja wypisującą zawartość drzewa.
# 2. Funkcja, która sprawdza czy dana liczba należy do drzewa.
# 3. Funkcja, która zwróci rozmiar drzewa (liczbę węzłów).
# 4. Funkcja, która zwróci wysokość drzewa (liczbę poziomów).
# 5. Funkcja, która zwróci liczbę liści drzewie.


class Node:
    def __init__(self,val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def elements(t):

    def rek(t):
        if t == None:
            return

        print(t.val)

        rek(t.right)
        rek(t.left)

    rek(t)

def czy_zawiera(t, num):
    if t == None:
        return False

    if t.val == num:
        return True

    return czy_zawiera(t.left, num) or czy_zawiera(t.right, num)

def rozmiar(t,i):
    if t.left == None and t.right == None:
        return i

    return rozmiar(t.left, i + 1) + rozmiar(t.right, i + 1)

def height(t,h):

    if t.left == None and t.right == None:
        return h

    maxi = 0

    if t.left != None and t.right != None:
            maxi = max(height(t.left, h + 1), height(t.right, h + 1), maxi)

    elif t.left != None:
            maxi = max(height(t.left, h + 1), maxi)
    else:
        maxi = max(height(t.right, h + 1), maxi)

    return maxi

