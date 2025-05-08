class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = new_node
    def printll(self):
        if self.head is None:
            return
        else:
            curr = self.head
            while curr is not None:
                print(curr.data,end="->")
                curr = curr.next
            print("none")
    def insert_at_first(self, data):
        new_node  = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self.head
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    def insert_at_k(self, data, k):
        new_node = Node(data)
        if self.head is None:
            if k == 1:
                self.head = new_node
            else:
                print("Invalid index: List is empty, can only insert at position 1")
            return
        if k == 1:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        for i in range(1, k - 1):
            if curr is None:
                print("Invalid index: Position out of range")
                return
            curr = curr.next
        if curr is None:
            print("Invalid index: Position out of range")
            return
        new_node.next = curr.next
        curr.next = new_node
    def deletion_at_head(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            return self.head
    def delete_at_last(self):
        if self.head is None:
            return None
        if self.head.next is None:
        # Only one node in the list
            self.head = None
            return
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
            return self.head
    def delete_node(self, val):
        if self.head is None:
            return None

        # If head node is the one to delete (whether alone or not)
        if self.head.data == val:
            self.head = self.head.next
            return self.head

        curr = self.head
        while curr.next is not None and curr.next.data != val:
            curr = curr.next

        if curr.next is None:
            print("val not found")
            return self.head

        # Delete the node
        temp = curr.next
        curr.next = curr.next.next
        temp.next = None  # Optional in Python
        return self.head
    def remove_duplicate(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.head
        slow = self.head
        fast = self.head.next
        while fast is not None:
            if slow.data == fast.data:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        return self.head
    def rotate(self, k):
        if self.head is None:
            return None
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return self.head
        new_tail = self.head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        tail.next = self.head
        new_tail.next = None
        return new_head






l1 = linkedlist()
l1.add_node(1)
l1.add_node(1)
l1.add_node(1)
l1.add_node(2)
l1.add_node(3)
l1.add_node(3)
# l1.printll()
# l1.insert_at_first(4)
# l1.printll()
# l1.insert_at_end(5)
# l1.printll()
# l1.insert_at_k(500,4)
# l1.printll()
# l1.deletion_at_head()
# l1.printll()
# l1.delete_at_last()
# l1.printll()
# l1.delete_node(40)
# l1.printll()
# l1.remove_duplicate()
l1.printll()
l1.head = l1.rotate(5)
l1.printll()