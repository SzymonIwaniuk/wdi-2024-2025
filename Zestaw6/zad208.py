#Proszę napisać funkcję, która usuwa z listy cyklicznej elementy, których klucz występuje
#dokładnie k razy. Do funkcji należy przekazać wskazanie na jeden z elementów listy, oraz liczbę k, funkcja
#powinna zwrócić informację czy usunięto jakieś elementy z listy.
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def check(keys,repetitions,key):
    if key in keys:
        i = 0
        while keys[i] != key:
            i += 1
        repetitions[i] += 1
    else:
        keys += [key]
        repetitions += [1]
    return keys,repetitions

def find_cycle(p):
    point = p
    run = p
    while run.next != point:
        run = run.next
    return run
def to_delete(keys,repetitions,k):
    tab = []
    l = len(keys)
    for i in range(l):
        if repetitions[i] == k:
            tab += [keys[i]]
    return tab

def zad208(p,k):

    if p == None:
        return p
    if k == 1:
        return Node()

    keys = []
    repetitions = []
    stop = find_cycle(p)
    run1 = p
    run2 = p
    prev = None
    while run1 != stop:
        keys, repetitions = check(keys,repetitions,run1.val)
        run1 = run1.next

    delete = to_delete(keys,repetitions,k)

    while run2 != stop:
        if run2.val in delete:
            if prev == None:
                p = p.next
            else:
                prev.next = run2.next
                run2 = run2.next
        else:
            prev = run2
            run2 = run2.next
    return p




a1 = Node(1, Node(3, Node(5, Node(7))))
a2 = Node(3, Node(4, Node(5, Node(6))))
a3 = Node(2, Node(3, Node(5, Node(8))))


while result != None:
     print(result.val)
     result = result.next