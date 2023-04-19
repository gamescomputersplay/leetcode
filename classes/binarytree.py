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
        ''' Text representation TODO
        '''
        return "Tree Node, Text representation TODO"

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
    demo_list = [1, 2, 3, None, 4, 5, None]
    print(f"This is a tree created from {demo_list}: {create_binary_tree(demo_list)}")