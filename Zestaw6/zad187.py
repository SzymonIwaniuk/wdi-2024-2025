class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def zad187(p):
    if p == None or p.next == None:
        return p
    if p.next.next == None:
        if p.val > p.next.val:
            p.next = None
        return p
    guardian = Node(0)
    guardian.next = p
    prev = guardian
    run = p
    while run != None and run.next != None:
        if run.val >= run.next.val:
            run.next = run.next.next
        else:
            prev = run
            run = run.next
    return guardian.next



a = Node(4)
b = Node(2)
c = Node(6)
d = Node(7)
a.next = b
b.next = c
c.next = d

result = zad187(a)

while result != None:
    print(result.val)
    result = result.next
