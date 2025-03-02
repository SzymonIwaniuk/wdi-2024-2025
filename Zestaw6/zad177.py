class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # Custom print method for debugging
        return str(self.val) + (" -> " + str(self.next) if self.next else "")

def newset():
    return Node(None)

def insert(p, val):
    while p.next and p.next.val < val:
        p = p.next
    if p.next and p.next.val == val:
        return  # val is already in the set
    else:
        if p.next:
            assert val < p.next.val
        p.next = Node(val, p.next)

p = newset()
for v in [2, 1, 3, 7, 4, 2, 0, -69]:    insert(p, v)
print(p)

