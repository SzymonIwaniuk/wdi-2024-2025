class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def insert_last(p,value):
    new_node = Node(value)
    if p is None:
        return new_node # edge case dla pustego node
    run = p
    start = run
    while run.next != None:
        run = run.next

    run.next = new_node
    return start

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

result = insert_last(a,5)

while result != None:
    print(result.val)
    result = result.next