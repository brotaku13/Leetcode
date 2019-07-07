"""
Partition linked list
Write code to partition a linked list around a value x so that all nodes less 
than x come before all nodes greater than or equal to x. if x is contained within 
the list, the values of x only need to be after the elements less than x
"""

import sys
sys.path.append('..')
import helpers

def partition(head, num):
    # get reference to last element in the list
    last = head
    while last.next is not None:
        last = last.next

    stop = last
    curr = head
    while curr.val >= 5:
        head = head.next
        last.next = curr
        curr.next = None
        last = last.next
        curr = head
    
    while curr.next != stop:
        if curr.next.val >= num:
            # swap to last
            swap = curr.next
            curr.next = swap.next
            last.next = swap
            last = last.next
            last.next = None
        else:
            curr = curr.next

def alternative(head, num):
    new_head = head
    new_tail = head

    while head is not None:
        nex = head.next
        if head.val >= num:
            new_tail.next = head
            new_tail = head
        else:
            head.next = new_head
            new_head = head
        head = nex

    new_tail.next = None
    return new_head


def main():
    l = helpers.list_from_array([3, 5, 8, 5, 10, 2, 1])
    helpers.print_list(l)
    num = 5
    print(num)
    # partition(l, num)
    helpers.print_list(alternative(l, 5))

main()