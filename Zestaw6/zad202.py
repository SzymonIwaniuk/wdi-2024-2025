#Zadanie 202. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W pierwszej
#liście liczby są posortowane rosnąco, a w drugiej nie. Proszę napisać funkcję usuwającą z obu list liczby
#występujące w obu listach. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
#łączną liczbę usuniętych elementów

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def zad202(p1, p2):
    if p1 is None or p2 is None:
        return 0

    cnt = 0
    # Usuwanie elementów z listy 1
    dummy1 = Node(0, p1)
    prev1 = dummy1
    while prev1.next:
        run2 = p2
        prev2 = None
        found = False
        while run2:
            if run2.val == prev1.next.val:  # Jeśli wartości się zgadzają
                # Usuń z listy 2
                if prev2 is None:
                    p2 = run2.next
                else:
                    prev2.next = run2.next
                found = True
                cnt += 1
                break
            prev2 = run2
            run2 = run2.next

        if found:  # Usuń z listy 1
            prev1.next = prev1.next.next
            cnt += 1
        else:
            prev1 = prev1.next

    # Aktualizacja głowy listy 1
    p1 = dummy1.next

    return cnt

# Przykład użycia
list1 = Node(1, Node(3, Node(5)))
list2 = Node(2, Node(3, Node(6)))

result = zad202(list1, list2)
print("Liczba usuniętych elementów:", result)

# Wydrukuj listę 1
print("Lista 1 po operacji:")
current = list1
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# Wydrukuj listę 2
print("Lista 2 po operacji:")
current = list2
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")