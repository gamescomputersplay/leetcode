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


def list_2_tree(array):
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

def level_order_2_tree(array):
    ''' Create a binary tree from a level-order representation.
    Return root node
    '''

    array_pointer = 1
    node_queue = [TreeNode(array[0])]
    queue_pointer = 0

    while queue_pointer < len(node_queue) and array_pointer < len(array):

        current_node = node_queue[queue_pointer]

        if current_node is None:
            queue_pointer += 1
            continue

        if array[array_pointer] is not None:
            current_node.left = TreeNode(array[array_pointer])
            node_queue.append(current_node.left)
        array_pointer += 1
        if array[array_pointer] is not None:
            current_node.right = TreeNode(array[array_pointer])
            node_queue.append(current_node.right)
        array_pointer += 1
        
        queue_pointer += 1

    return node_queue[0]


if __name__ == "__main__":
    print("This library is a definition and some helpers to work with binary trees")
    print("Here's a short demo:\n")
    demo_list = [1, 2, 3, None, 4, 5, None, 6, 7, None, 8]
    print(f"This is a tree created from list representation {demo_list}:\n{list_2_tree(demo_list)}\n")
    demo_level_order = [1,None,1,1,1,]
    print(f"This is a tree created from level-order representation {demo_level_order}:")
    print(f"{level_order_2_tree(demo_level_order)}\n")
