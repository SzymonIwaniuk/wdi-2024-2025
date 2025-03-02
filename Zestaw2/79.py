#Program przechodzi po elementach tablicy a nastepnie przechodzi znowu po jej elementach
# sprawdzajac czy kazdy czynnik pierwszy wystepuja dokladnie raz, jezeli nie to wylicza maxi
#koniec koncow zwracajac najdluzszy podciag 




def arePrimes(iloczyn):#Funkcja sprawdza czy w iloczynie wystepuje kazdy czynnik pierwszy
    i = 2               #dokladnie raz jezeli nie zwraca False
    while iloczyn > 1:
        cnt = 0 
        while iloczyn % i == 0:
            cnt += 1
            iloczyn //= i
        if cnt > 1:
            return False
        i += 1
        
    return True 


def spojny(T):
    N = len(T)
    maxi = cnt = 0
    iloczyn = 1
    for i in range(N):#przechodze po kazdym elemencie tablicy  
        iloczyn *= T[i]
        if arePrimes(iloczyn): #jezeli arePrimes == True zwiekszam cnt
                cnt += 1
        else:
            maxi = max(maxi, cnt) # jezeli nie: cnt przypisz 0, iloczyn przypisz 1 - 
            cnt = 0               # przechodze do nastpnego elementu i sprawdzam dalej
            iloczyn = 1
        maxi = max(maxi, cnt)         #edge case gdy elementy podciagu bylyby na ostatnim miejscu w tablicy
    return maxi

print(spojny([2,23,33,35,7,4,6,7,5,11,13,22]))

