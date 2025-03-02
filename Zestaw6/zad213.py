#Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej: class Node:
#..def init(self,val,next=None): ....self.val = val ....self.next = next Lista zawierała wartości stanowiące kolejne
#wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto pewną liczbę elementów. Proszę napisać funkcję re-
#pair(p), (p wskazuje na pierwszy element listy) która uzupełnia listę elementami, tak aby ponownie zawierała
#olejne wyrazy ciągu arytmetycznego. Funkcja powinna zwrócić liczbę wstawionych elementów. Komentarz:
#Można założyć, że lista wejściowa liczy więcej niż 2 elementy
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def nwd(a,b):
    while b != 0 :
        a, b = b, a % b
    return a

def diff(tab):
    l = len(tab)
    if l == 1:
        return tab[0]
    new_tab = []
    i = 0
    while i + 1 < l:
        new_tab += [nwd(tab[i], tab[i + 1])]
        i += 2
    return diff(new_tab)

def repair(p):
    seq = []
    run = p
    while run != None: #Przekazanie pozostałych wyrazów ciagu do tablicy
        seq += [run.val]
        run = run.next

    roznice = []
    l = len(seq)
    for i in range(l - 1):
        roznice += [seq[i+1] - seq[i]] #Roznice miedzy pozostalymi wyrazami ciagu

    roznica = diff(roznice) #Obliczanie docelowej roznicy

    #Tworzenie i umieszczanie brakujacych wyrazow ciagu art
    run2 = p
    ile = 0 #ile elementow zostalo wstawionych
    while run2.next != None:
        cur_seg = run2.val
        next_seg = run2.next.val
        how_many_segments_missing = ((next_seg - cur_seg) // roznica) - 1
        if how_many_segments_missing > 0:
            guardian = Node() # wartownik
            head = guardian # wskaznik na początek wartownika
            for j in range(how_many_segments_missing):
                guardian.next = Node(cur_seg + roznica) # tworzenie i umieszczenie brakującego wyrazu
                guardian = guardian.next
                cur_seg += roznica
                ile += 1

            tmp = run2.next
            run2.next = head.next
            guardian.next = tmp

        run2 = run2.next #przejście do następnego elementu
    return ile

a = Node(2)
b = Node(4)
c = Node(6)
d = Node(8)
e = Node(10)

a.next = b
b.next = c
c.next = d
d.next = e

result = repair(a)
print(result)




