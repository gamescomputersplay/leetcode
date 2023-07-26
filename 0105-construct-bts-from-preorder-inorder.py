''' https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''

from classes.binarytree import TreeNode

class Solution:
    def buildTree(self, preorder, inorder):

        # End of recursion if tree is empty or has 1 node
        if len(preorder) == 0:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        # Find the root (0 element of preorder)
        # Adn find it in inorder too
        root = preorder[0]
        root_index = inorder.index(root)

        # Split inorder in two by that root value
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index + 1:]

        # Make set copy of those
        set_left, set_right = set(inorder_left), set(inorder_right)

        # Sort preorder into two new lists
        # use sets for faster sorting
        preorder_left, preorder_right = [], []
        for val in preorder:
            if val in set_left:
                preorder_left.append(val)
            elif val in set_right:
                preorder_right.append(val)

        # Recussively build a tree
        node = TreeNode(root)
        node.left = self.buildTree(preorder_left, inorder_left)
        node.right = self.buildTree(preorder_right, inorder_right)

        return node

def main():
    ''' Test buildTree
    '''
    solution = Solution()

    test_cases = [
        ([3,9,20,15,7], [9,3,15,20,7]),
        # ([-1], [-1],)
    ]
    for preorder, inorder in test_cases:
        result = solution.buildTree(preorder, inorder)
        print(preorder, inorder, result)


if __name__ == "__main__":
    main()