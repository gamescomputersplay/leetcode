''' https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
'''

class Solution:
    def search(self, nums, target):

        left,right = 0, len(nums)

        leftmost, rightmost = 0, len(nums) - 1

        #while True:
        for _ in range(20):

            center = (left + right) // 2
            print(left, center, right)

            if nums[center] == target:
                return True

            if right - left == 1:
                return False

            # Left half
            if nums[leftmost] < nums[center]:
                if target < nums[leftmost]:
                    left = center
                elif target < nums[center]:
                    right = center
                else:
                    left = center
            # Right half
            elif nums[center] < nums[rightmost]:
                if target > nums[rightmost]:
                    right = center
                elif target > nums[center]:
                    left = center
                else:
                    right = center

            # Not enough info
            #else:
            #???

def main():
    ''' Test search
    '''
    solution = Solution()

    test_cases = [
    #    ([2,5,6,0,0,1,2], 0),
    #    ([2,5,6,0,0,1,2], 3),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 1),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 2),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 3),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 4),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 5),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 6),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 7),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 8),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 9),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 10),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 0),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 11),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 7.5),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 3.5),
    #    ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 5.5),
        [(1,0,1,1,1), 0]
    ]

    for nums, target in test_cases:
        result = solution.search(nums, target)
        print(nums, target, result)

if __name__ == "__main__":
    main()
