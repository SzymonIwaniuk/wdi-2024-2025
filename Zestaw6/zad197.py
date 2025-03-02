
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def zad197(p):
    slow = p
    fast = p.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    i = 0
    point = slow
    while slow.next != point:
        i += 1
        slow = slow.next
    run = p

    while run != fast:
        i += 1
        run = run.next

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
f.next = c

print(zad197(a))

# while result != None:
#     print(result.val)
#     result = result.next
