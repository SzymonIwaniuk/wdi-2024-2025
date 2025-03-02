#Zadanie 117. W tablicy o rozmiarze NxN wypełnionej liczbami naturalnymi umieszczono dokładnie jeden
#fragment ciągu Fiboacciego o długości co najmniej 3 elementów. Ciąg ten może leżeć w tablicy pionowo lub
#poziomo w kierunku rosnącym lub malejącym. Proszę napisać funkcje, która dla zadanej tablicy odszuka ten
#fragment i zwróci jego długość

def isFib(b, c):
    x = y = 1
    while c >= y:
        if c == y and b == x:
            return True
        x,y = y,x+y

    return False


def findfib(T):
    N =len(T)

    for i in range(N - 2):
        for j in range(N - 2):
            a, b, c = T[i][j], T[i+1][j+1], T[i+2][j+2]
            if a + b == c and isFib(b, c):
                length = 3
                i += 1
                j += 1
                while i < N - 2 and j < N - 2:
                    a, b = b, c
                    c = T[i+2][j+2]
                    if a + b == c: length += 1
                    else: break

    return length

T = [[3,0,3,0],
     [5,5,0,0],
     [1,0,8,8],
     [1,2,3,13]]
print(findfib(T))