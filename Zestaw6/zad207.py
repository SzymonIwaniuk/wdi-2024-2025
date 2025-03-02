#Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” od pierwszej litery s2.
#Według tej zasady rozmieszczono napisy w liście cyklicznej, na przykład:
#??bartek??leszek??marek??ola??zosia?? ????????????????????????????????????? Proszę napisać stosowne
#definicje typów oraz funkcję wstawiającą do listy napis z zachowaniem zasady poprzedzania. Do funkcji należy
#przekazać wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą, czy
#udało się wstawić napis do listy. Po wstawieniu elementu wskaźnik do listy powinien wskazywać na nowo
#wstawiony element.
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def gowno(p,string):
    if p == None:
        return Node(string)
    slow = p
    fast = p.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    run = p.next
    prev = p
    new_string = Node(string)


    while run != slow.next:
        word1 = run.val
        word2 = prev.val
        if string >= word1 and string <= word2:
            prev.next = new_string
            new_string.next = run
            return p
        prev = run
        run = run.next
    if string <= run.val:
        prev.next = new_string
        new_string.next = run
        return new_string

    return p

a = Node('bartek')
b = Node('leszek')
c = Node('marek')
d = Node('ola')
e = Node('zosia')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = a

result = gowno(a, 'artur')
while result != None:
    print(result.val)
    result = result.next