''' https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def getDirections(self, root, startValue, destValue):

        path_to, path_from = None, None

        node_history = [root]
        current_path = []

        visited = set()

        while True:
            if node_history[-1].val == startValue:
                path_from = "".join(current_path)
            if node_history[-1].val == destValue:
                path_to = "".join(current_path)
            if path_to is not None and path_from is not None:
                break
            
            if node_history[-1].left is not None and node_history[-1].left.val not in visited:
                node_history.append(node_history[-1].left)
                visited.add(node_history[-1].val)
                current_path.append("L")
            elif node_history[-1].right is not None and node_history[-1].right.val not in visited:
                node_history.append(node_history[-1].right)
                visited.add(node_history[-1].val)
                current_path.append("R")
            else:
                node_history.pop()
                current_path.pop()

        shared_path = 0
        for i in range(min(len(path_to), len(path_from))):
            if path_to[i] == path_from[i]:
                shared_path += 1
            else:
                break

        total_path = "U" * (len(path_from) - shared_path) + path_to[shared_path:]

        return total_path

def main():
    ''' Test getDirections
    '''
    solution = Solution()

    test_cases = [
        ([5,1,2,3,None,6,4], 3, 2),
        ([2,1], 2, 1)
            ]
    for list_tree, startValue, destValue in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        result = solution.getDirections(tree, startValue, destValue)
        print(str(tree)[:50], result)

def huge_case():
    ''' Test with the really big case
    '''
    solution = Solution()

    startValue = 29716
    destValue = 54117

    tree = binarytree.level_order_2_tree(list_tree)
    result = solution.getDirections(tree, startValue, destValue)
    print(result)

if __name__ == "__main__":
    main()
    huge_case()