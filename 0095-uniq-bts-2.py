''' https://leetcode.com/problems/unique-binary-search-trees-ii/
'''


from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def generateTrees(self, n):

        def rec_tree(values):
            ''' Get the list of values
            return list of trees with these values
            '''

            if len(values) == 0:
                return [None]
            if len(values) == 1:
                return [TreeNode(values[0])]

            resulting_trees = []
            # Break values into left and right
            for i, value in enumerate(values):
                lefts = rec_tree(values[:i])
                rights = rec_tree(values[i+1:])

                # Build the tree of all combinations of left and right parts
                for left in lefts:
                    for right in rights:

                        tree = TreeNode(value)
                        tree.left = left
                        tree.right = right
                        resulting_trees.append(tree)

            return resulting_trees

        return rec_tree([n for n in range(1, n + 1)])

def main():
    ''' Test generateTrees
    '''
    solution = Solution()

    test_cases = [
       #1,
       #2,
       #3,
       4

    ]
    for n in test_cases:
        result = solution.generateTrees(n)
        print(f"{n}: {[str(tree) for tree in result]}")

if __name__ == "__main__":
    main()
