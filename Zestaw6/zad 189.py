class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def check(n):
    cnt1 = cnt2 = 0
    while n:
        if n % 3 == 1:
            cnt1 += 1
        elif n % 3 == 2:
            cnt2 += 2
        n //= 3
    if cnt1 > cnt2:
        return True
    return False

def zad189(p):
    if p == None:
        return p
    if p.next == None:
        if check(p.val):
            return Node()
        else:
            return p
    run = p.next
    prev = p
    while run != None:
        if check(run.val):
            prev.next = run.next
            run = run.next
        else:
            run = run.next
            prev = prev.next
    if check(p.val):
        p = p.next
        return p
    return p


a = Node(3)
b = Node(7)

a.next = b

result = zad189(a)

while result != None:
    print(result.val)
    result = result.next

