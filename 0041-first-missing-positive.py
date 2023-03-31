''' https://leetcode.com/problems/first-missing-positive/
'''

class Solution:
    def firstMissingPositive(self, nums):

        # Check "no positive" list
        max_value = max(nums)
        if max_value <= 0:
            return 1
        
        # Find the minimal positive number
        min_positive = min(n for n in nums if n > 0)

        # Check trivial case if min_positive > 1
        if min_positive > 1:
            return 1
        
        # Next, rearrange items as [1, 2, 3, 4, ...] etc
        for i in range(len(nums)):

            # Ignore non-positive numbers
            if nums[i] <= 0:
                continue

            # Ignore numbers that are already in place
            if nums[i] == i + 1:
                continue

            # Ignore numbers are bigger than the length on nums
            if nums[i] > len(nums):
                continue

            # Otherwise, do the chain switcheroo thingy
            # Meaning move a number in a number-1 place,
            # move the number that was there a num-1 place too and so on
            number_to_place = nums[i]
            while 1 <= number_to_place <= len(nums) and nums[number_to_place - 1] != number_to_place:

                buffer = nums[number_to_place - 1]
                nums[number_to_place - 1] = number_to_place
                number_to_place = buffer

        # Now go through the list, and first number that is nums[i] != i+1
        # i+1 will be the first missing positive
        for pos, num in enumerate(nums):
            if pos + 1 != num:
                return pos + 1
        
        # If all were in place, we have a 1..n list of integers,
        # so n+1 is the next missing one
        return len(nums) + 1


    def firstMissingPositive_brute(self, nums):
        ''' Inefficient brute force solution
        '''
        nums_copy = nums.copy()
        nums_copy.sort()
        for i in range(len(nums_copy)):
            if nums_copy[i] <=0:
                continue
            if i > 0 and nums_copy[i] > 1 and nums_copy[i - 1] <=0:
                return 1
            if i == 0 and nums_copy[i] > 1:
                return 1
            if i > 0 and nums_copy[i] > 1 and nums_copy[i] > nums_copy[i - 1] + 1:
                return nums_copy[i - 1] + 1
        return max(1, nums_copy[-1] + 1)


def random_test(runs):
    solution = Solution()

    for _ in range(runs):
        test_case = [random.randint(-10,10) for _ in range(random.randint(1,10))]
        #print("Test: ", test_case)

        control = solution.firstMissingPositive_brute(test_case)
        result = solution.firstMissingPositive(test_case)
        #print(test_case, result, control, result == control)

        if result != control:
            print("Error!")
            break
    else:
        print(f"{runs} tests okay")

def main():
    ''' Test firstMissingPositive
    '''
    solution = Solution()

    test_cases = [
        [1,2,0],
        [3,4,-1,1],
        [7,8,9,11,12],
        [6,3,4,5,1,2],
        [1],
        [-1],
        [2],
        [-10, -9, -9, -5, -2, -6]
    ]
    for array in test_cases:
        control = solution.firstMissingPositive_brute(array)
        result = solution.firstMissingPositive(array)
        print(array, result, control, result == control)

if __name__ == "__main__":
    import random
    main()
    random_test(10000)
