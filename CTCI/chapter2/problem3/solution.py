"""
Remove Middle node
given a singly linked list, delete a node in the middle of the list, 
given only access to that node (no access to head of list, or the node before the node given)
"""

import sys
sys.path.append('..')
import helpers

def remove_node(node):
    # copy data from next node over and then 
    # delete the next nod
    node.val = node.next.val
    node.next = node.next.next
    # del node.next
    

def main():
    l = helpers.list_from_array([3, 4, 5, 6, 7, 8, 9, 0])
    helpers.print_list(l)
    curr = l
    for i in range(3):
        curr = curr.next
    print(curr.val)
    remove_node(curr)
    helpers.print_list(l)

main()