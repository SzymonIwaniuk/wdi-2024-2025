class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def repair(p):
    prev = None
    run = p
    g1 = Node() # wartownik
    head = g1

    while run != None:
        if run.val % 2 == 0:
            head.next = Node(run.val)
            head = head.next

            if prev == None:
                p = p.next

            else:
                prev.next = run.next
        else:
            prev = run
        run = run.next
    if prev == None:
        return g1.next

    prev.next = g1.next

    return p

p = Node(2, Node(1))

# Wywołanie funkcji
list1 = repair(p)

# Funkcja do wypisywania listy
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Wynikowe listy
print_list(list1)
