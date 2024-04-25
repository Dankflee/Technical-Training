class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_head(head, data):
    # Create a new node with the given data
    new_node = ListNode(data)
    
    # If the linked list is empty, set the new node as the head and return it
    if head is None:
        return new_node
    
    # Set the next pointer of the new node to point to the current head
    new_node.next = head
    
    # Set the new node as the new head of the linked list
    return new_node

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Print the original linked list
print("Original linked list:")
print_linked_list(head)

# Insert a new node before the head with data value 0
head = insert_at_head(head, 0)

# Print the modified linked list
print("Linked list after inserting a new node before the head:")
print_linked_list(head)
