class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def delete_last(p):
    if p == None:
        return None
    if p.next == None:
        return p
    run = p
    while run.next.next != None:
        run = run.next
    run.next = None
    return p

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
result = delete_last(a)
while result != None:
    print(result.val)
    result = result.next
