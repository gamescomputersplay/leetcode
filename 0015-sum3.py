''' https://leetcode.com/problems/3sum/
'''

class Solution:
    def threeSum(self, nums):

        # Dict of all option of lacking to 0 for all pairs of numbers:
        # {[how much lack to 0: ((positions), (values)) ... ]}
        lack = {}

        # Answers (use set to deduplicate)
        answers = set()

        # Go through all pairs and populate "lack"
        for position_1, num_1 in enumerate(nums):
            for position_2, num_2 in enumerate(nums[:position_1]):

                if - num_1 - num_2 not in lack:
                    lack[- num_1 - num_2] = []
                lack[- num_1 - num_2].append(((position_1, position_2), (num_1, num_2)))

        for position, num in enumerate(nums):

            # If number is in "lack" - we have an answer
            if num in lack:
                for lack_option in lack[num]:
                    if position not in lack_option[0]:

                        one_answer = list(lack_option[1])
                        one_answer.append(num)
                        one_answer.sort()
                        answers.add(tuple(one_answer))

        # Transform into the right format
        return [list(answer) for answer in answers]

def main():
    ''' Test threeSum
    '''
    solution = Solution()

    test_cases = [
        [1, 2, 4, 6, 12, 10, -3, -22, -11, -3, -5],
        [-1, 0, 1, 2, -1, -4], # [[-1,-1,2],[-1,0,1]]
        [0, 1, 1], # []
        [0, 0, 0], # [[0,0,0]]
        [3, 0, -2, -1, 1, 2], # [[-2,-1,3],[-2,0,2],[-1,0,1]]
    ]
    for nums in test_cases:
        result = solution.threeSum(nums)
        print(nums, result)

def large_case(case_size):
    ''' Time the large case
    '''
    nums = [random.randint(-10000, 10000) for i in range(case_size)]
    solution = Solution()
    start = time.time()
    solution.threeSum(nums)
    elapsed = time.time() - start
    return elapsed

def test_timing(max_power = 12):
    ''' Run a series of ever larger cases
    '''
    for power in range(2, max_power):
        size = 2**power
        elapsed = large_case(size)
        print(F"{power}:{size} {elapsed}")

if __name__ == "__main__":
    import random
    import time
    main()
    test_timing(13)
