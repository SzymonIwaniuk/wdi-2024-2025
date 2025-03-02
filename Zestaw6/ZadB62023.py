class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def check(num): # 2 = parzysta dodatnia # 1 = nieparzysta ujemna # 0 = ani taka ani taka
    if num % 2 == 0:
        if num > 0:
            return 2
        else:
            return 0
    else:
        if num < 0:
            return 1
    return 0

def devide(p):
    cycle1, cycle2 = Node(), Node() # wartowniki
    start1, start2 = cycle1, cycle2
    tmp = p
    while p != None and tmp != p.next:
        result = check(p.val)
        if result == 1:
            start1.next = Node(p.val)
            start1 = start1.next
        elif result == 2:
            start1.next = Node(p.val)
            start2 = start2.next
    else:
        p = p.next
    return cycle1.next, cycle2.next

def separate(p):
    return divide(p)




