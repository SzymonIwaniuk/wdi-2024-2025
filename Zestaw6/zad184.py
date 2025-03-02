class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def reverse(p):
    run = p
    prev = None
    while run:
        next_node = run.next
        run.next = prev
        prev = run
        run = next_node

    return prev

def add(p1,p2):
    run1 = reverse(p1)
    run2 = reverse(p2)
    guard = Node()
    head = guard
    r = 0

    while run1 or run2:
        val1 = run1.val if run1 else 0
        val2 = run2.val if run2 else 0
        sume = val1 + val2 + r
        r = sume // 10
        new_node = Node(sume % 10)
        head.next = new_node
        head = head.next
        if run1:
            run1 = run1.next
        if run2:
            run2 = run2.next

    if r:
        head.next = Node(r)

    return reverse(guard.next)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

e = Node(1)
f = Node(2)
g = Node(3)
h = Node(4)

e.next = f
f.next = g
g.next = h
result = add(a,e)
while result != None:
    print(result.val)
    result = result.next