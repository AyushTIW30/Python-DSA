
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
head = taking_input()


# Function to print linked list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# Printing the linked list to verify
print_linked_list(head)
