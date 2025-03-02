#Zadanie 138. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w
#sensie liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów
#tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego
#podzbioru. Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10

def zbiory(T):

    def rek(index, sum_el, sum_ind, amount):

        if index == len(T):
            if sum_el == sum_ind and amount > 0:
                return amount, sum_el
            return 1e10, 1e10

        amount_with, sum_el_with = rek(index + 1, sum_el + T[index], sum_ind + index, amount + 1)

        amount_without, sum_el_without = rek(index + 1, sum_el, sum_ind, amount)

        if amount_with < amount_without:
            return amount_with, sum_el_with
        return  amount_without, sum_el_without


    result = rek(0,0,0,0)
    return result[1]

print(zbiory([1,7,3,5,11,2]))
