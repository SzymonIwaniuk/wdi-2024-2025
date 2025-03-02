
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

#Zadanie 195. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą.
#Proszę napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia
#jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej

def zad195(p):
    if p == None or p.next == None:
        return p
    index = (None, None)
    lenght = maxi = 1
    i = 0
    head = p
    while head != None and head.next != None:
        i += 1
        if head.val < head.next.val:
            lenght += 1
        else:
            if lenght > maxi:
                index = (i - lenght, i)
                maxi = lenght
                lenght = 1
        head = head.next
    print(index)
    run1 = p
    run2 = p
    for j in range(index[0] - 1):
        run1 = run1.next
    for u in range(index[1]):
        run2 = run2.next

    run1.next = run2

    return p
a = Node(5)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(4)
f = Node(3)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

result = zad195(a)

while result != None:
    print(result.val)
    result = result.next
