#Zadanie 206. Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w liście ułożone są
#według rosnących potęg. Proszę napisać funkcję obliczającą różnicę dwóch dowolnych wielomianów. Wielo-
#miany reprezentowane są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo utworzonej
#listy reprezentującej wielomian wynikowy. Listy wejściowe powinny pozostać niezmienione.
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def roznica(p1,p2): # p1 - p2
    run1 = p1
    run2 = p2
    guardian = Node()
    head = guardian

    while run1 != None or run2 != None:
        if run1 == None:
            guardian.next = Node(-run2.val)
            guardian = guardian.next
            run2 = run2.next
        elif run2 == None:
            guardian.next = Node(run1.val)
            guardian = guardian.next
            run1 = run1.next
        else:
            guardian.next = Node(run1.val - run2.val)
            guardian = guardian.next
            run1,run2 = run1.next, run2.next

    return head.next

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

p1 = Node(1, Node(3, Node(5, Node(10))))
p2 = Node(4, Node(2, Node(6)))
result_list = roznica(p1, p2)

print_list(result_list)