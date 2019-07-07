"""
Return Kth from last
given a singly linked list, return the kth from last element in the list
"""

import sys
sys.path.append('..')
import helpers

def k_from_last(head, k):
    current = head
    while current is not None and k > 0:
        k -= 1
        current = current.next
    follow = head
    while current is not None:
        current = current.next
        follow = follow.next

    return follow.val

def main():
    l = helpers.list_from_array([3, 4, 5, 6, 7, 8, 9, 0])
    print(k_from_last(l, 3))

main()