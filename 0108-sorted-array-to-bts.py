''' https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''

from classes import binarytree
from classes.binarytree import TreeNode

class Solution:
    def sortedArrayToBST(self, nums):

        if not nums:
            return None

        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node

def main():
    ''' Test sortedArrayToBST
    '''
    solution = Solution()

    test_cases = [
        list(range(1)),      
        list(range(2)),      
        list(range(3)),      
        list(range(10)),  
        [-10,-3,0,5,9],    
    ]
    for nums in test_cases:
        tree = solution.sortedArrayToBST(nums)
        print(f"{nums} {tree}")

if __name__ == "__main__":
    main()
