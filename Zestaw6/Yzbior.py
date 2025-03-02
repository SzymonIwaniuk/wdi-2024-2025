class Node():
    def __init__(self, val = None, next=None):
        self.val = val
        self.next = next

def common_part(p):
    guard = Node()
    head = guard

    while p != None:
        head.next = Node(p.val)
        head = head.next
        p = p.next

    return guard.next

def part(z1,z2):
    run1 = z1
    flag = False

    while run1 != None:
        run2 = z2
        while run2 != None:
            if run1 == run2:
                flag = True
                break
            run2 = run2.next
        if flag:
            break

        run1 = run1.next
    if flag == False:
        return z1, z2 #brak części wspólnej

    head1 = z1
    while head1.next != run1:
        head1 = head1.next

    head2 = z2
    while head2.next != run1:
        head2 = head2.next

    head1.next = common_part(run1)
    head2.next = common_part(run1)

    return z1,z2

a = Node(8)
b = Node(5)
c = Node(2)

e = Node(9)
f = Node(6)

a1 = Node(7)
b1 = Node(1)
c1 = Node(4)
d1 = Node(3)

a.next = b
b.next = c
c.next = e
e.next = f

a1.next = b1
b1.next = c1
c1.next = d1
d1.next = e

list1, list2 = part(a,a1)

# Funkcja do wypisywania listy
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Wynikowe listy
print("List1 (dokładnie dwa razy):")
print_list(list1)
print("List2 (pozostałe):")
print_list(list2)