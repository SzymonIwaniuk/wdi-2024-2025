class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def repair(p):
    # Initialize pointers
    current = p
    count_inserted = 0

    while current and current.next:
        # Calculate the ratio between consecutive terms
        if current.val == 0:
            raise ValueError("Current value cannot be zero in a geometric progression.")

        ratio = current.next.val / current.val

        if not (ratio == int(ratio)):
            raise ValueError("Non-integer ratio detected, sequence not valid for repair.")

        ratio = int(ratio)

        # Check if the next value matches the expected progression
        expected_next_val = current.val * ratio

        while current.next and current.next.val != expected_next_val:
            # Create a new node with the expected value
            new_node = Node(expected_next_val)

            # Insert the new node into the list
            new_node.next = current.next
            current.next = new_node

            # Update the count of inserted elements and calculate the next expected value
            count_inserted += 1
            expected_next_val *= ratio

        # Move to the next node
        current = current.next

    return count_inserted

# Example usage:
# Construct the list 4 -> -32 -> -2048
head = Node(4)
head.next = Node(-32)
head.next.next = Node(-2048)

# Repair the list
inserted_count = repair(head)
print(f"Number of inserted elements: {inserted_count}")

# Print the repaired list
current = head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next
