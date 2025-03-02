class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def check(n):
    cnt = 0
    while n:
        if n % 8 == 5:
            cnt += 1
        n //= 8
    if cnt % 2 == 0:
        return True
    else:
        return False

def zad190(p):
    if p == None:
        return p


    new_head = None
    run = p
    prev = None
    while run != None:
        if check(run.val):
            if prev:
                prev.next = run.next
            else:
                p = run.next

            tmp = run.next
            run.next = new_head
            new_head = run
            run = tmp
        else:
             prev = run
             run = run.next
    if new_head != None:
        last = new_head
        while last.next != None:
            last = last.next
        last.next = p
    return new_head if new_head != None else p 



a = Node(77)
b = Node(45)
c = Node(4973)
d = Node(333)
a.next = b
b.next = c
c.next = d
result = zad190(a)

while result != None:
   print(result.val)
   result = result.next

