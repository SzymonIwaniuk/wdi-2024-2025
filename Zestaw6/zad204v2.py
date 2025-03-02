class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def zad204(p1,p2):
    run1 = p1
    while run1 != None:

        value = run1.val
        run2 = p2
        prev = None
        while run2 != None:
            if value < run2.val:
                prev = run2
                run2 = run2.next
            elif value > run2.val:
                if prev != None:
                    new_node = Node(value)
                    prev.next = new_node
                    new_node.next = run2
                    break
                else:
                    new_node = Node(value)
                    new_node.next = p2
                    p2 = new_node
            else:
                break

        return p2