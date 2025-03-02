#Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułamki
#reprezentowane są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję zwraca-
#jącą długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geometryczny. W przypadku
#gdy w tablicy nie ma takiego podciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość 0. Można
#założyć, że tablica wejściowa liczy więcej niż 2 elementy

def podciag(T):
    cnt = maxi = 2
    N = len(T)
    
    for u in range(1, N - 1):
        q = (T[u][0] / T[u][1]) / (T[u - 1][0] / T[u - 1][1]) if T[u - 1][0] != 0 else None

        if q == None: continue

        else:
            if (T[u][0] / T[u][1]) * q == (T[u + 1][0] / T[u + 1][1]): cnt += 1
                
            else: cnt = 2

        maxi = max(maxi, cnt)

    return maxi if maxi > 2 else 0




print(podciag([(1,1),(1,2),(1,4),(1,8),(6,9),(2,1),(4,1),(8,1)]))
