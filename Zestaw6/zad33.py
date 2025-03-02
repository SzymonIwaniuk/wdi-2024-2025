class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def insert_word(p, string):
    first = string[0]
    last = string[-1]
    start = p
    run = p
    while True:
        word1 = run.val
        word2 = run.next.val
        if ord(word1[-1]) < ord(first) and ord(last) > ord(word2[1]):
            a = Node(string)
            a.next = run.next
            run.next = a
            return True
        run = run.next
        if run == start:
            return False
