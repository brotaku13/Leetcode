"""
Sum Lists: 
you have two numbers represented by a linked list where each node holds a single value. 
the digits are stored in reverse order such that the 1's digit is at the front of the list. 
write a function that adds the two numbers and returns them as a linked list
"""

import sys
sys.path.append('..')
import helpers

def reverse_sum_lists(l1, l2):
    res = None
    head = res
    value = carry = 0
    while l1 is not None:
        s = l1.val + l2.val + carry
        carry = s // 10
        value = s % 10
        if res is None:
            res = helpers.Node(value, None)
            head = res
        else:
            res.next = helpers.Node(value, None)
            res = res.next
        
        l1 = l1.next
        l2 = l2.next

    if carry != 0:
        res.next = helpers.Node(carry, None)

    return head 

def main():
    l_617 = helpers.list_from_array([7, 1, 6])
    l_295 = helpers.list_from_array([5, 9, 2])

    helpers.print_list(reverse_sum_lists(l_617, l_295))

    l_617 = helpers.list_from_array([6, 1, 7])
    l_295 = helpers.list_from_array([2, 9, 5])
    helpers.print_list(forward_sum_list(l_617, l_295))

main()