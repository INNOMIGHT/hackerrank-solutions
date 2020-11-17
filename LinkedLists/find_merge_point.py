def find_merge_points(head1, head2):
    pointer1 = head1
    pointer2 = head2

    while pointer1 != pointer2:
        if pointer1.next is None:
            pointer1 = head2
        else:
            pointer1 = pointer1.next
        if pointer2.next is None:
            pointer2 = head1
        else:
            pointer2 = pointer2.next
    return pointer2

