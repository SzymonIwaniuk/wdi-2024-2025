class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def reverse(p):
    prev = None
    run = p

    while run != None:
        next_node = run.next
        run.next = prev
        prev = run
        run = next_node

    return prev

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

result = reverse(a)
while result != None:
    print(result.val)
    result = result.next