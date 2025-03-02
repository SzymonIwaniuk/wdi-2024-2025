class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

#Dane są dwie niepuste listy, z których każda zawiera niepowtarzające się elementy. Elementy
#w pierwszej liście są uporządkowane rosnąco, w drugiej elementy występują w przypadkowej kolejności. Proszę
#napisać funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane elementy będą stanowić
#sumę mnogościową elementów z list wejściowych. Do funkcji należy przekazać wskazania na obie listy, funkcja
#powinna zwrócić wskazanie na listę wynikową. Na przykład dla list
def is_include(value,p):
    if p == None:
        return False
    if p.next == None:
        if p.val == value:
            return True
        return False

    run = p

    while run.next != None and run.val < value:
        run = run.next
    return run.val == value

def insert(value,p):
    if p == None:
        return Node(value)

    run = p
    prev = None
    new_node = Node(value)

    while run != None and value > run.val:
        prev = run
        run = run.next
    if prev == None:
        new_node.next = p
        return new_node
    if run != None:
        prev.next = new_node
        new_node.next = run
        return p

    prev.next = new_node
    return p



def result(p1,p2):
    if p2 == None:
        return p1

    run2 = p2
    while run2 != None:
        if not is_include(run2.val,p1):
            p1 = insert(run2.val,p1)
        run2 = run2.next

    return p1


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

p1 = Node(1, Node(3, Node(5, Node(10))))
p2 = Node(4, Node(2, Node(6)))
result_list = result(p1, p2)

print_list(result_list)