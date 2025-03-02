class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def list_to_ll(List: list):
    """Convert list to linked list"""
    head = current = Node(List[0])
    for i in range(1, len(List)):
        new = Node(List[i])
        current.next = new
        current = new
    return head

def bubble_sort_swap_val(head):
    if head == None or head.next == None:
        return head

    swapped = True

    while swapped:
        swapped = False
        current = head

        while current and current.next:
            if current.val > current.next.val:
                current.val, current.next.val = current.next.val, current.val
                swapped = True

            current = current.next

    return head

def bubble_sort_swap_nodes(head):
    if head is None or head.next is None:
        swapped = True

        while swapped:
            swapped = False
            previousNode = head




p = list_to_ll([4,2,5,1,3])

result = bubble_sort_swap_val(p)
while result != None:
     print(result.val)
     result = result.next
