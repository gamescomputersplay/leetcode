''' Classes for working with Linked lists
'''

class ListNode:
    ''' Definition for singly-linked list
    '''

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        ''' Looks  something like:
        1 -> 2 -> 3 -> 4 ->
        '''

        string = ""
        current = self

        while current is not None:

            string += f"{current.val} -> "
            current = current.next

        return string


def create_linked_list(array):
    ''' Put together a linked list from a regular list,
    return the first link.
    '''

    # LInked list can't be empty
    if not array:
        return None

    # This is teh link we'll return in the end
    first = ListNode(array[0])

    # Previous is the one ready to be extended
    previous = first

    # First element is taken care of, start from the second one
    for value in array[1:]:

        # New links are created
        current = ListNode(value)
        # Attached to the last link of the existing linked list
        previous.next = current
        # And now they are the link ready to be extended
        previous = current

    # But it is the first one we need to return
    return first
