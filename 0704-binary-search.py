''' https://leetcode.com/problems/binary-search/
'''

class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums)

        while True:

            center = (left + right) // 2

            # Needle found
            if nums[center] == target:
                return center

            # No room to narrow down, but no needle
            if right-left == 1:
                return -1

            if nums[center] > target:
                right = center
            else:
                left = center

        return -1

def main():
    ''' Test search
    '''
    solution = Solution()

    test_cases = [
        ([-1,0,3,5,9,12], 9), # 4
        ([-1,0,3,5,9,12], 2), # -1
        ([1], 1),
        ([1], 2),    
        ([1], 0),  
        ([1, 2], 2),
        ([1, 3], 2),
        ([1, 2, 3], 4),
        ([1, 2, 3], -4),
        ([1, 2, 3], 1),
        ([-11, -2, 3], 1),
    ]
    for array, target in test_cases:
        result = solution.search(array, target)
        print(f"{array}, {target}, {result}")

if __name__ == "__main__":
    main()
