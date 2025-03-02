class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def zad192(p):
    if p == None or p.next == None:
        return p

    uniq = []
    prev = None
    run = p
    while run != None:
        if run.val in uniq:
            prev.next = run.next
            run = run.next
        else:
            uniq = uniq + [p.val]
            prev = run
            run = run.next
    return p

a = Node(3)
b = Node(7)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

result = zad192(a)

while result != None:
    print(result.val)
    result = result.next
