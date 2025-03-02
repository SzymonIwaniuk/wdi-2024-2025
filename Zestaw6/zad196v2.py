#Zadanie 196. Dana jestlista, który być może zakończona jest cyklem. Napisać funkcję, która spraw-
#dza ten fakt.
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def zad196(p):
    slow = p
    fast = p
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast.next == None or fast.next.next == None:
        return False
    else:
        return True




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = d

print(zad196(a))




