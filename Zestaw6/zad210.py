#Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o uporządkowanych rosnąco elementach.
#Proszę napisać funkcję iloczyn(z1,z2,z3), która przekształca 3 listy (zbiory) z1,z2,z3 w jedną listę (zbiór)
#zawierającą elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić wskazanie do listy
#wynikowej
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def common_part(p1,p2):
    if p1 == None:
        return None
    if p2 == None:
        return None

    guardian = Node() # wartownik
    head = guardian
    while p1 != None and p2 != None:
        if p1.val < p2.val: # Jezeli p1.val < p2.val to przechodzą do następnego
            p1 = p1.next
        elif p1.val > p2.val:
            p2 = p2.next
        else:
            head.next = Node(p1.val)
            head = head.next
            p1 = p1.next
            p2 = p2.next

    return guardian.next

def iloczyn(z1,z2,z3):
    return common_part(z1,common_part(z2,z3)) # z1 n z2 n z3 = z1 n (z1 n z2)

a1 = Node(1, Node(3, Node(5, Node(7))))
a2 = Node(3, Node(4, Node(5, Node(6))))
a3 = Node(2, Node(3, Node(5, Node(8))))

result = iloczyn(a1,a2,a3)

while result != None:
     print(result.val)
     result = result.next