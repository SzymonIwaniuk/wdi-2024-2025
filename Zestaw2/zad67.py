def czynniki(n):
    if n <= 1: return []

    czynnik = [False for _ in range(n + 1)]
    dzielnik = 2
    
    while dzielnik <= n:
        if n % dzielnik == 0:
                czynnik[dzielnik] = True
        while n % dzielnik  == 0:
            n //= dzielnik

        dzielnik += 1

    
    return czynnik


def czy_skok(T):
    l = len(T)

    czy_moze_skoczyc = [False for _ in range(l)]
    czy_moze_skoczyc[0] = True

    i = 0

    while i < l:
        if czy_moze_skoczyc[i]:
            czynnik = czynniki(T[i])
            for j in range(len(czynnik)):
                if czynnik[j] and i + j < l:
                    czy_moze_skoczyc[i + j] = True
        i += 1
        
    return czy_moze_skoczyc[l-1]

print(czy_skok([4,9,10,3,5,12,2,11]))
            
