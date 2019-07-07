class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_from_array(array):
    if len(array) == 0:
        return None
    
    head = Node(array[0], None)

    current = head
    for i in range(1, len(array)):
        current.next = Node(array[i], None)
        current = current.next

    return head

def print_list(head):
    while(head is not None):
        print('{}->'.format(head.val), end='')
        head = head.next
    print('n')

