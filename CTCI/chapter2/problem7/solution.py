"""
Intersection
given two singly linked lists, determine if the two lists intersect. Return the intersecting node. 
https://leetcode.com/problems/intersection-of-two-linked-lists
"""

import sys
sys.path.append('..')
import helpers

def get_tail_size(head):
    if head is None:
        return 0, None
    current = head
    count = 1

    while current.next is not None:
        current = current.next
        count += 1
    
    return count, current

def get_intersection(head1, head2):
    if head1 is None or head2 is None:
        return None
    
    tail1, len1 = get_tail_size(head1)
    tail2, len2 = get_tail_size(head2)
    if tail1 != tail2:
        return None

    shorter = head1 if len1 <= len2 else head2
    longer = head1 if len2 > len1 else head2

    for i in range(abs(len1 - len2)):
        longer = longer.next
    
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next
    return shorter
