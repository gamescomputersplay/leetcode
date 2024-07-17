''' https://leetcode.com/problems/rotate-array/
'''

class Solution:
    def rotate_slow(self, nums, k):
        for _ in range(k):
            nums.insert(0, nums.pop())

    def rotate(self, nums, k):
        size = (len(nums)-k) % len(nums) 
        nums.extend(nums[:size])
        del nums[:size]


def main():
    ''' Test rotate
    '''
    solution = Solution()

    test_cases = [
        ([1,2,3,4,5,6,7], 3),
        ([-1,-100,3,99], 2),
        ([1,2], 3)
    ]
    for nums, k in test_cases:
        print(nums, k)
        solution.rotate(nums, k)
        print(nums, "\n")

if __name__ == "__main__":
    main()
