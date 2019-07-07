"""
Remove Dups
write code ro remove duplicates from an unsorted linked list
what would you do if a temp buffer is not allowed?
"""

import sys
sys.path.append('..')
import helpers

def remove_dups(head):
    bv = 0
    current = head
    bv = bv | 1 << current.val
    while current.next is not None:
        if (bv >> current.next.val) & 1 == 1:
            # need to remove next node
            temp = current.next
            current.next = temp.next
            del temp
        else:
            # mark that we have found a new val
            bv = bv | 1 << current.next.val
            current = current.next

    return head

def alternative(head):
    s = set()
    current = head
    follow = None
    while current is not None:
        if current.val in s:
            follow.next = current.next
        else:
            follow = current
            s.add(current.val)
        current = current.next

    return head

def main():
    l = helpers.list_from_array([1, 1, 4, 5, 6, 7, 7, 3, 4, 6, 8, 9, 9])
    helpers.print_list(l)
    # helpers.print_list(remove_dups(l))
    helpers.print_list(alternative(l))

main()