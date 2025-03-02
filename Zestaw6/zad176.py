class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # Custom print method for debugging
        return str(self.val) + (" -> " + str(self.next) if self.next else "")

def newset():
    return Node(None)

def insert(p, val):
    while p.next != None and p.next.val < val:
        p = p.next
    if p.next and p.next.val == val:
        return  # val is already in the set
    else:
        if p.next:
            assert val < p.next.val
        p.next = Node(val, p.next)

def swap(p, n):
    i = 0  # Initialize the index counter
    while p:  # Traverse the list until p becomes None
        if i == n:
            p.val = "value"  # Modify the value at the nth position
            break
        else:
            i += 1
            p = p.next

# Create the list
p = newset()
for v in [2, 1, 3, 7, 4, 2, 0, -69]:
    insert(p, v)

# Print the list
print("Before swap:", p)

# Swap the value at position 3
swap(p, 3)

# Print the modified list
print("After swap:", p)

def n_element(p, n):
    i = 0  # Initialize the index counter
    while p:  # Traverse the list until p becomes None
        if i == n:  # Check if we've reached the nth element
            return p.val
        else:
            i += 1
            p = p.next

print(n_element(p,4))