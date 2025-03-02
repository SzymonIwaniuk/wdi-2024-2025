class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def wskaznik(p):

    if p == None or p.next == None:
        return None

    slow = p
    fast = p

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast == None or fast.next == None:
        return None

    slow = p
    while slow != fast:
        slow = slow.next
        fast = fast.next

    head = p
    while head.next != slow:
        head = head.next
    # element przed cyklem


    return (head.val, slow.val)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = d

print(wskaznik(a))