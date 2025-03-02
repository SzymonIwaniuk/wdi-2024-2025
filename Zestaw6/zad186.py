class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def check(word1,word2):
        if word1 < word2:
            return 2
        elif word1 > word2:
            return 1
        else:
            return 0

def zad186(p,string):
    seg = Node(string)
    if p == None:
        return seg
    if p.next == None:
        if check(p.val, string) == 1:
            p.next = seg
        else:
            seg.next = p
            return seg
        return p

    start = p
    run = p
    while run.next:
        if run.val == string or run.next.val == string:
            return start
        word1 = run.val
        word2 = run.next.val
        flag1 = check(word1,string)
        flag2 = check(string,word2)
        if flag1 == 2 and flag2 == 1:
            seg.next = run.next
            run.next = seg
            return start
        run = run.next
    run.next = seg

    return start

a = Node('ala')
b = Node('basia')
c = Node('kasia')
a.next = b
b.next = c

result = zad186(a,'aala')

while result != None:
    print(result.val)
    result = result.next
