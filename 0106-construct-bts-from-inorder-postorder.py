''' https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
'''

from classes.binarytree import TreeNode

class Solution:
    def buildTree(self, inorder, postorder):

        # End of recursion if tree is empty or has 1 node
        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        # Find the root (last element of postorder)
        # Adn find it in inorder too
        root = postorder[-1]
        root_index = inorder.index(root)

        # Split inorder in two by that root value
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index + 1:]

        # Make set copy of those
        set_left, set_right = set(inorder_left), set(inorder_right)

        # # Sort preorder into two new lists
        # # use sets for faster sorting
        postorder_left, postorder_right = [], []
        for val in postorder:
            if val in set_left:
                postorder_left.append(val)
            elif val in set_right:
                postorder_right.append(val)

        # # Recussively build a tree
        node = TreeNode(root)
        node.left = self.buildTree(inorder_left, postorder_left)
        node.right = self.buildTree(inorder_right, postorder_right)

        return node

def main():
    ''' Test buildTree
    '''
    solution = Solution()

    test_cases = [
        ([9,3,15,20,7], [9,15,7,20,3]),
        ([-1], [-1],)
    ]
    for inorder, postorder in test_cases:
        result = solution.buildTree(inorder, postorder)
        print(inorder, postorder, result)


if __name__ == "__main__":
    main()