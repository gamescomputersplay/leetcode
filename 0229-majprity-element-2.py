''' https://leetcode.com/problems/majority-element-ii/
'''

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        
        prev = None
        count = 0
        majority = set()

        for num in nums:

            if num != prev:
                prev = num
                count = 1
            else:
                count += 1
            if count > len(nums) / 3:
                majority.add(num)

        return list(majority)

    def majorityElement_linear_space(self, nums):

        majority = set()
        count = {}
        treshold = len(nums) / 3
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > treshold:
                majority.add(num)
        return list(majority)

def main():
    ''' Test majorityElement
    '''
    solution = Solution()

    test_cases = [
        [3,2,3],
        [1],
        [1,2],
        [1, 2, 3],
    ]

    for n in test_cases:
        result = solution.majorityElement(n)
        print(n, result)

if __name__ == "__main__":
    main()
