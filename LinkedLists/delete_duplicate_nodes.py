def removeDuplicates(head):
    pointer = head
    if head is None:
        return None
    while pointer.next:
        if pointer.data == pointer.next.data:
            pointer.next = pointer.next.next
        else:
            pointer = pointer.next
    return head
