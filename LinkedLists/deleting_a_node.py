class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def delete_node(self, position):
        pointer = self.head
        for i in range(position - 1):
            pointer = pointer.next
        temp_next = pointer.next.next
        pointer.next = None
        pointer.next = temp_next

    def print_list(self, head):
        print_val = self.head
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next
