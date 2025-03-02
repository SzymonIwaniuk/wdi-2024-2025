class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def insert_key(p,key):
    seg = Node(key)
    if p == None: #pusty node
        return Node(key)
    start = p
    while p.next != None:
        if p.next.val == key :
            p.next = p.next.next
            return start
        p = p.next
    p.next = seg
    return start

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# a.next = b
# b.next = c
# c.next = d

result = insert_key(a,5)

while result != None:
    print(result.val)
    result = result.next