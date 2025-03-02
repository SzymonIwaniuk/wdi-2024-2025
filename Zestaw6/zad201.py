#Zadanie 201. Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do
#funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do
#scalonej listy. - funkcja iteracyjna, - funkcja rekurencyjna
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def zad201(p1,p2):
    if p1 == None:
        return p2
    if p2 == None:
        return p1
0
    guardian = Node()
    head = guardian
    run1 = p1
    run2 = p2

    while run1 != None and run2 != None:
        el1 = run1.val
        el2 = run2.val
        if el1 < el2:
            new_node = Node(el1)
            head.next = new_node
            head = head.next
            run1 = run1.next
        elif el2 < el1:
            new_node = Node(el2)
            head.next = new_node
            head = head.next
            run2 = run2.next
        else:
            n1 = Node(el1)
            n2 = Node(el2)
            head.next = n1
            n1.next = n2
            head = head.next.next
            run1 = run1.next
            run2 = run2.next

    while run1 != None:
        new_node = Node(run1.val)
        head.next = new_node
        head = head.next
        run1 = run1.next

    while run2 != None:
        new_node = Node(run2.val)
        head.next = new_node
        head = head.next
        run2 = run2.next

    return guardian.next

a1 = Node(1, Node(3, Node(5, Node(7))))
a2 = Node(3, Node(4, Node(5, Node(6))))

result = zad201(a1,a2)

while result != None:
     print(result.val)
     result = result.next
