class Node():
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def check_order(string):
    l = len(string)
    for i in range(l-1): #rosnący
        if string[i] > string[i+1]:
            break

    if i == l - 2: return 0

    for j in range(l-1): #malejący
        if string[j] < string[j+1]:
            break

    if j == l - 2: return 1

    #ani taki ani taki
    return 2


def make_order(p):

    seg0 = Node() # wartownik
    seg1 = Node("")
    seg2 = Node("")
    head0, head1, head2 = seg0, seg1, seg2

    while p != None:
        string = p.val
        which = check_order(string)
        new_node = Node(string)
        if which == 0:
            head0.next = new_node
            head0 = head0.next
        elif which == 1:
            head1.next = new_node
            head1 = head1.next
        else:
            head2.next = new_node
            head2 = head2.next
        p = p.next

    head0.next = seg2
    head2.next = seg1
    return seg0.next

a = Node('ala')
b = Node('ola')
c = Node('abcd')
d = Node('ula')
e = Node('irys')
h = Node('ewa')
f = Node('sroka')
g = Node('gips')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = h
h.next = f
f.next = g
result = make_order(a)

while result != None:
    print(result.val)
    result = result.next