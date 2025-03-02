class Node():
    def __init__(self):
        self.val = None
        self.next = None

def check(s):
    l = len(s)
    if l == 1 or s[0] == s[1]:
        return 1
    lock = True if ord(s[0]) < ord(s[1]) else False
    for i in range(l - 1):
        if lock and s[i + 1] <= s[i]: ###abcd
            return 1
        if not lock and s[i + 1] >= s[i]:
            return 1
    if lock:
        return 0
    return 2

def make_order(p):
    seg1 = Node() # wartownik
    seg1.next = Node()
    seg2 = seg1.next
    seg2.val = ""
    seg3 = seg2.next
    seg3.val = ""
    while p != None:
        variant = check(p.val)
        if variant == 0:
            q = seg1
        elif variant == 1:
            q = seg2
        else:
            q = seg3
        tmp = q.next
        q.next = p
        p.next, p = tmp, p.next
    return seg1.next

# OBSŁUGA TESTOWANIA
def board_to_list(T): # Przepisuje zadaną tablicę jako listę odsyłaczową
    p = Node()
    head = p
    l = len(T)
    for i in range(l):
        p.next = Node()
        p = p.next
        p.val = T[i]
    return head.next

def printlist(p): # Wypisuje kolejne węzły listy
    while p != None:
        print (f"{p.val} -> ", end="")
        p = p.next
    return

# KONIEC OBSŁUGI TESTOWANIA

T = ["ala", "ola", "abel", "ula", "irys", "ewa", "sroka", "gips"]
p = board_to_list(T)
x = make_order(p)
printlist(x)

