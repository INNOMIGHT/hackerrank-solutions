class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def reverse_list(self, head):
        if head is None:
            return
        else:
            self.reverse_list(head.next)
            print(head.data)

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
linked_list = SinglyLinkedList()
linked_list.head = a
linked_list.print_list()
linked_list.reverse_list(a)
