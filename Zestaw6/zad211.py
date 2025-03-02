class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def check(n):
    return n % 2 == 0


def repair(p):
    guardian = Node()
    head = guardian
    prev = None
    run = p
    while run != None:
        if check(run.val):
            head.next = Node(run.val)
            head = head.next
            if prev == None:
                p = run.next
            else:
                prev.next = run.next
        else:
            prev = run
        run = run.next
    if prev == None:
        return guardian.next
    prev.next = guardian.next
    return p

a = Node(2)
b = Node(2)
c = Node(1)
d = Node(5)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

result = repair(a)

while result != None:
     print(result.val)
     result = result.next