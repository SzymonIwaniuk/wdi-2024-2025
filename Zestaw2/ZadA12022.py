def sequence(T):
    lenght = 0
    a = None
    b = None
    N = len(T)
    
    for i in range(N - 3): #z zalozenia ze ciag jest minimum 3 wyrazowy 
        for j in range(i + 3, N):
            cnt = 0
            
            q = T[j] / T[i] if T[i] != 0 else None #wyznaczenie iloczynu oraz sprawdzenie dzielenia przez 0

            if q is None: continue #w wypadku dzielenia przez 0 przejscie do nastepnej iteracji


            tmp_i, tmp_j = i, j #zmienne pomocnicze

            while tmp_j + 1 < N and T[tmp_j + 1] / T[tmp_i + 1] == q:#sprawdzenie warunku nie wyjscia poza tablice oraz kolejnego wyrazu ciagu
                cnt += 1
                tmp_i += 1
                tmp_j += 1
                
            if cnt > lenght: # jezeli znaleziony ciag byl wiekszy od poprzedniego to zmieniamy dlugosc oraz początkowy i koncowy indeks ciągu
                lenght = cnt
                a, b = i, cnt + i

    return a, b

print(sequence([2,5,7,3,2,3,5,7,6,6,9,15,21,18,19,23,2,6,4,8,3,5,7,1,3,2]))

                
                
