#Zadanie 188. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
#wartościach typu int, usuwającą wszystkie elementy, których wartość dzieli bez reszty wartość bezpośrednio
#następujących po nich elementów
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def devide(n1,n2):
    return n2 % n1 == 0

def zad188(p):
    if p == None or p.next == None:
        return p

    run = p
    while run != None and run.next != None:
        if devide(run.val,run.next.val):
            run.next = run.next.next
        else:
            run = run.next
    return p 
a = Node(2)
b = Node(4)
c = Node(7)
d = Node(8)
e = Node(9)
a.next = b
b.next = c
c.next = d
d.next = e

result = zad188(a)

while result != None:
    print(result.val)
    result = result.next

