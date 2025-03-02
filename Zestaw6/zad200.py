#Zadanie 200. Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji
#należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def check(p1,p2):

    run1 = p1

    while run1 != None:

        if run1.val == p2.val:
            tmp1 = run1
            tmp2 = p2

            while tmp1 != None and tmp2 != None and tmp1.val == tmp2.val:
                tmp1 = tmp1.next
                tmp2 = tmp2.next
            if tmp2 == None:
                return True

        run1 = run1.next

    return False

def zad200(p1,p2):
    if p1 == None or p2 == None:
        return True
    l1 = l2 = 0
    run1, run2 = p1, p2

    while run1 != None:
        l1 += 1
        run1 = run1.next

    while run2 != None:
        l2 += 1
        run2 = run2.next

    if l1 >= l2:
        return check(p1,p2)
    return check(p2,p1)


a = Node(2)
b = Node(3)
c = Node(4)
d = Node(5)
e = Node(5)

f = Node(1)
h = Node(2)
i = Node(3)
j = Node(4)

a.next = b
b.next = c
c.next = d

f.next = h
h.next = i
i.next = j
j.next = e

print(zad200(a,f))
