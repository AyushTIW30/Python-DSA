
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def taking_input():
    l = [int(ele) for ele in input().split()]
    head = None
    curr = None  # Keeping track of the last node

    for i in range(len(l)):
        new_node = Node(l[i])
        if head is None:  # ✅ Fixed 'in' to 'is'
            head = new_node
            curr = new_node  # First node is both head and tail
        else:
            curr.next = new_node  # Attach new node at the end
            curr = new_node  # Move tail to new last node

    return head  # ✅ Returning head so we can use it


# Calling the function and storing the linked list

# Function to print linked list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# Printing the linked list to verify

def last_node(h):
    if h is None:
        return None
    curr = h
    while curr.next is not None:
        curr = curr.next
    return curr.data

def sec_last(h):
    if h is None or h.next is None:
        return None
    curr = h
    while curr.next.next is not None:
        curr = curr.next
    return curr.data

def second_node_data(h):
    if h is None or h.next is None:
        return None
    return h.next.data

def count_node(h):
    count = 0
    curr = h
    while curr is not None:
        count += 1
        curr = curr.next
    return count

def search_node(ele, h):
    while h is not None:
        if h.data == ele:
            return "Element found"
        h = h.next
    return "Element not found"

def swap_data(h):
    curr = h
    while curr is not None and curr.next is not None:
        curr.data, curr.next.data = curr.next.data, curr.data
        curr = curr.next.next
    return h

def reverse(h):
    prev = None
    curr = h
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def insert_head(h, x):
    new_node = Node(x)
    new_node.next = h
    return new_node

def insert_last(h, x):
    new_node = Node(x)
    if h is None:
        return new_node
    curr = h
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
    return h

# Main code to run
head = taking_input()
print("Initial Linked List:")
print_linked_list(head)

# Example operations
print("Count of nodes:", count_node(head))
print("Last node data:", last_node(head))
print("Second last node data:", sec_last(head))
print("Second node data:", second_node_data(head))
print(search_node(3, head))

head = insert_head(head, 99)
print("After inserting 99 at head:")
print_linked_list(head)

head = insert_last(head, 7)
print("After inserting 7 at end:")
print_linked_list(head)

head = swap_data(head)
print("After swapping alternate nodes:")
print_linked_list(head)

head = reverse(head)
print("After reversing the list:")
print_linked_list(head)
