''' https://leetcode.com/problems/recover-binary-search-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def recoverTree(self, root):

        def find_fault(node, allowed_min, allowed_max, is_root=False):
            ''' Return node with a problem
            '''
            
            # Recursively check for problems in left and right branches
            # Deeper problems should overtake shallow problems
            left_problem = None
            right_problem = None
            if node.left is not None:
                left_problem = find_fault(node.left, allowed_min, node.val)
            if node.right is not None:
                right_problem = find_fault(node.right, node.val, allowed_max)

            # No deeper problems. Is ihis node a problem
            if left_problem is None and right_problem is None:
                if node.val < allowed_min:
                    return node
                if node.val > allowed_max:
                    return node
                return None
            #print(left_problem, right_problem)


            # If in problem in both branches - fix it
            if left_problem is not None and right_problem is not None:
                left_problem.val, right_problem.val = right_problem.val, left_problem.val
            # If problem is in only one branch - fix it only if on root
            elif is_root and left_problem is not None and left_problem.val > node.val:
                left_problem.val, node.val = node.val, left_problem.val
            elif is_root and right_problem is not None and right_problem.val < node.val:
                right_problem.val, node.val = node.val, right_problem.val

            # Otherwise, pass it to the next level
            else:
                if left_problem is None:
                    return right_problem
                if right_problem is None:
                    return left_problem

            return None

        find_fault(root, float("-inf"), float("inf"), is_root=True)
        return None


def main():
    ''' Test recoverTree
    '''
    solution = Solution()

    test_cases = [
        # [2,3,1], #1-3
        [1,3,None,None,2], # 1-3
        # [3,1,4,None,None,2], # 2-3
        # [5, 10, 8, 2, 4, 7, 9, 1, None, None, None, 6, None, None, 3], # 3-10
        # [3,None,2,None,1], # 1-3

    ]
    for list_tree in test_cases:
        tree = binarytree.level_order_2_tree(list_tree)
        print(f"IN: {tree}")
        solution.recoverTree(tree)
        print(f"OUT: {tree}\n")

if __name__ == "__main__":
    main()
