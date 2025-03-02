class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def zad182(p):
    # If the list is empty or has only one node, return it as is
    if p is None or p.next is None:
        return p

    current = p
    while current is not None and current.next is not None:
        # Skip the second node by making current.next point to the node after next
        current.next = current.next.next
        # Move current to the next node (which was the third node before deletion)
        current = current.next

    return p


# Setting up the linked list
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

# Deleting every second element
result = zad182(a)

# Print the result
while result != None:
    print(result.val)
    result = result.next