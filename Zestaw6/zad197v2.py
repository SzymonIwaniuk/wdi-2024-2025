#Zadanie 197. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę ele-
#mentów w cyklu
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def zad197(p):
    slow = p
    fast = p
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: break
    if fast == None or fast.next == None:
        return 0

    slow = p
    while slow != fast:
        slow = slow.next

    i = 1
    head = slow.next
    while head != slow:
        i += 1
        head = head.next
    return i

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

print(zad197(a))