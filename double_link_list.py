class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Added for doubly linked list

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr  # Link backwards

    def printll(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        self.add_node(data)

    def insert_at_k(self, data, k):
        new_node = Node(data)
        if k == 1:
            self.insert_at_first(data)
            return
        curr = self.head
        for _ in range(k - 2):
            if curr is None:
                print("Invalid index")
                return
            curr = curr.next
        if curr is None:
            print("Invalid index")
            return
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node

    def deletion_at_head(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_last(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None

    def delete_node(self, val):
        curr = self.head
        while curr and curr.data != val:
            curr = curr.next
        if curr is None:
            print("Value not found")
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev

    def remove_duplicate(self):
        curr = self.head
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
                if curr.next:
                    curr.next.prev = curr
            else:
                curr = curr.next

    def rotate(self, k):
        if self.head is None:
            return
        # Find length and tail
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return
        # Find new tail
        new_tail = self.head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        # Break and rearrange
        new_tail.next = None
        new_head.prev = None
        tail.next = self.head
        self.head.prev = tail
        self.head = new_head



dll = DoublyLinkedList()
for val in [1, 2, 3, 4, 5, 6]:
    dll.add_node(val)

dll.printll()         # Before rotation

         # After rotation
