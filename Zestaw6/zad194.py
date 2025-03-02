class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def arrays(a,b):
    a1, a2= a[0], a[1]
    b1, b2 = b[0], b[1]
    if a1 >= b1 and a2 <= b2:
        return b
    if a1 <= b1 and a2 >= b2 and a2 >= b1:
        return a
    if a1 < b1  and a2 < b2 and b2 >= a1:
        return (a1,b2)
    if b1 < a1 and b2 < a2:
        return (b1,a2)
    return 0 # rozłączne


def zad194(p):
    if p == None or p.next == None:
        return p

    def rek(head,flag):
        if flag == False:
            return head

        guardian = Node()
        tail = guardian
        run1 = head
        has_new_nodes = False

        while run1 != None:
            run2 = run1.next

            while run2 != None:
                merged = arrays(run1.val,run2.val)

                if merged != 0:
                    has_new_nodes = True
                    current = guardian.next
                    already_exists = False
                    while current is not None:
                        if current.val == merged:
                            already_exists = True
                            break
                        current = current.next
                    if not already_exists:
                        tail.next = Node(merged)
                        tail = tail.next
                run2 = run2.next
            run1 = run1.next
        return rek(guardian.next, has_new_nodes)
    return rek(p,True)

a = Node((15,19))
b = Node((2,5))
c = Node((7,11))
d = Node((8,12))
e = Node((5,6))
f = Node((13,17))
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

wynik = zad194(a)

while wynik != None:
    print(wynik.val)
    wynik = wynik.next
