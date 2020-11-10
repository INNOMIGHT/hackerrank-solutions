class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        new_node = Node(data)
        tail.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        counter = 0
        pointer = self.head
        while pointer is not None:
            counter += 1
            if counter == position:
                new_node.next = pointer.next
                pointer.next = new_node
            pointer = pointer.next

    def print_list(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = None
obj = SinglyLinkedList()
obj.head = a
obj.insert_at_head(0)
obj.insert_at_tail(5)
obj.insert_at_position(4, 4)
obj.print_list()