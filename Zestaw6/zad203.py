#Zadanie 203. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W obu listach
#liczby są posortowane rosnąco. Proszę napisać funkcję usuwającą z każdej listy liczby nie występujące w
#drugiej. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę usuniętych
#elementów

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def zad203(p1,p2):
    guardian1, guardian2 = Node(), Node()
    guardian1.next, guardian2.next = p1, p2
    prev1, run1 = guardian1, p1
    prev2, run2 = guardian2, p2
    cnt = 0

    while run1 != None and run2 != None:

        if run1.val == run2.val:
            prev1, run1 = run1, run1.next
            prev2, run2 = run2, run2.next

        elif run1.val < run2.val:
            prev1.next = run1.next
            run1 = run1.next
            cnt += 1
        else:
            prev2.next = run2.next
            run2 = run2.next
            cnt += 1

    while run1 != None:
        prev1.next = run1.next
        run1 = run1.next
        cnt += 1

    while run2 != None:
        prev2.next = run2.next
        run2 = run2.next
        cnt += 1

    return cnt


list1 = Node(1, Node(3, Node(5)))
list2 = Node(2, Node(3, Node(6)))
print(zad203(list1,list2))