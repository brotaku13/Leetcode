"""
Loop Detection
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop
https://leetcode.com/problems/linked-list-cycle-ii/
"""

def get_start(head):
    # first move them until they are k into the loop
    if head is None:
        return None
    
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if slow != fast or fast is None or fast.next is None:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow