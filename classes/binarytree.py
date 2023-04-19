''' Classes for working with Binary Trees
'''

class TreeNode:
    ''' Definition for a binary tree node.
    '''

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        ''' Text representation of a tree node
        '''

        def add_item(array, item, position):
            ''' Add item to the array at the position "position",
            pad non-exiting position before it with None
            '''
            while len(array) < position:
                array.append(None)
            array.append(item)

        list_representation = []

        queue_pointer = 0
        queue = [(self, 0)]

        while len(queue) > queue_pointer:

            item, item_position = queue[queue_pointer]
            add_item(list_representation, item.val, item_position)

            if item.left is not None:
                queue.append((item.left, item_position * 2 + 1))
            if item.right is not None:
                queue.append((item.right, item_position * 2 + 2))

            queue_pointer += 1

        return "Tree Node: " + str(list_representation)


def create_binary_tree(array):
    ''' Create a binary tree from a list.
    Return root node
    '''
    def recursive_node_create(n):
        ''' Recursive function that create a node for element n in the array
        '''
        if n >= len(array) or array[n] is None:
            return None
        
        node = TreeNode(array[n])
        node.left = recursive_node_create(2*n + 1)
        node.right = recursive_node_create(2*n + 2)

        return node

    return recursive_node_create(0)


if __name__ == "__main__":
    print("This library is a definition and some helpers to work with binary trees")
    print("Here's a short demo:")
    demo_list = [1, 2, 3, None, 4, 5, None, 6, 7, None, 8]
    print(f"This is a tree created from {demo_list}: {create_binary_tree(demo_list)}")