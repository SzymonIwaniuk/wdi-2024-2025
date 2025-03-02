from math import log10
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def first(n):
    l = int(log10(n) + 1)
    first = n // (10**(l-1))
    return first

def last(n):
    return n % 10


def insert(p,n):
    if p == None:
        return 0
    if p.next == None:
        return 0

    run1 = p
    point = p
    while last(run1.val) != first(n):
        run1 = run1.next
        if run1.next == point: return 0


    start = run1
    point2  = start
    run2 = start
    i = 0
    new_node = Node(n)
    while last(n) != first(run2.val) or i < 2:
        i += 1
        run2 = run2.next
        if run2 == point2:
            return 0

    start.next = new_node
    new_node.next = run2

    #return i - 2
    return p
a = Node(2023)
b = Node(31)
c = Node(11)
d = Node(11)
e = Node(37)
f = Node(707)
# g = Node(72)
# h = Node(29)
# i = Node(902)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = a
# f.next = h
# h.next = i
result = insert(a,307)
while result != None:
     print(result.val)
     result = result.next
print(result)