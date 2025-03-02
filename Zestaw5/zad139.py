#Zadanie 139. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników
#niż 2, 3, 5. Jedynka też jest taką liczbą. Proszę napisać funkcję rekurencyjną, wypisującą liczby znajdujące
#się w przedziale od 1 do N włącznie.

def generuj(N):
    def rek(num, tab):
        if num > N:
            return tab

        if num not in tab:
            print(num)

        l = len(tab)
        new_tab = [0 for _ in range(l+1)]
        for i in range(l):
            new_tab[i] = tab[i]
        new_tab[-1] = num

        new_tab = rek(num * 2, new_tab)
        new_tab = rek(num * 3, new_tab)
        new_tab = rek(num * 5, new_tab)

        return new_tab

    rek(1,[])

generuj(1000)
