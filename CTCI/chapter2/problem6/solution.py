"""
Palindrome
Implement a function to check if a linked list is a palindrome
"""

import sys
sys.path.append('..')
import helpers

def stack_impl(head):
    s = []
    slow = head
    fast = head
    if head.next is None:
        return True

    s.append(slow)
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        s.append(slow)

    if fast.next is None:
        # odd list, so pop element from s
        s.pop(-1)
    
    fast = slow.next
    while fast is not None:
        if fast.val != s[-1].val:
            return False
        fast = fast.next
        s.pop(-1)
    return True

def main():
    l = helpers.list_from_array(list('gobbbbog'))
    helpers.print_list(l)
    print(stack_impl(l))

main()