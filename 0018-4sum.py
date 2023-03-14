''' https://leetcode.com/problems/4sum/
'''

class Solution:
    def fourSum(self, nums, target):

        # Filter and restructure data as {num: [positions], }
        # Make sure there are no more than 4 positions kept for each number

        nums_dict = {}
        for position, number in enumerate(nums):
            if number not in nums_dict:
                nums_dict[number] = []
            if len(nums_dict[number]) < 4:
                nums_dict[number].append(position)
        #print(nums_dict)

        # Generate dict of "pairs" like this
        # {sum or inversed sum of 2 numbers minus target/2: 
        # ([(position 1, position 2)], [(position 3, position 4)])}
        # Where the first list is for the sum (num1 + num2- target-2)
        # and the second list of for inverse sums (-num1-num2 + target /2)

        pair_values = {}

        for number_1, positions_1 in nums_dict.items():
            for position_1 in positions_1:
                for number_2, positions_2 in nums_dict.items():
                    for position_2 in positions_2:
                        if position_1 == position_2:
                            continue
                        weird_sum = number_1 + number_2 - target / 2
                        if weird_sum not in pair_values:
                            pair_values[weird_sum] = [[],[]]
                        pair_values[weird_sum][0].append((position_1, position_2))
                        if -weird_sum not in pair_values:
                            pair_values[-weird_sum] = [[],[]]
                        pair_values[-weird_sum][1].append((position_1, position_2))

        #print(pair_values)

        # Set (to deduplicate) of answer
        answers = set()
        for pair_value, positions in pair_values.items():
            if len(positions) < 2:
                continue
            # Cross-reference all position pairs
            for position_1, position_2 in positions[0]:
                for position_3, position_4 in positions[1]:
                    if position_1 not in (position_3, position_4) and \
                       position_2 not in (position_3, position_4):
                        #print(pair_value, position_1, position_2, position_3, position_4)
                        answer = [nums[position_1], nums[position_2], nums[position_3], nums[position_4]]
                        answer.sort()
                        answers.add(tuple(answer))

        return [list(answer) for answer in answers]

    def fourSumBrute(self, nums, target):

        solutions = set()

        for a, num_1 in enumerate(nums):
            for b, num_2 in enumerate(nums[:a]):
                for c, num_3 in enumerate(nums[:b]):
                    for d, num_4 in enumerate(nums[:c]):

                        if num_1 + num_2 + num_3 + num_4 == target:
                            solution = [num_1, num_2, num_3, num_4]
                            solution.sort()
                            solutions.add(tuple(solution))

        return [list(solution) for solution in solutions]

def main():
    ''' Test threeSum
    '''
    solution = Solution()

    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0), # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        ([2, 2, 2, 2, 2, 2], 8), # [[2,2,2,2]]
        ([1, 2, 3, 4, 5, 6, 7, 8], 13),
    ]
    for nums, target in test_cases:
        result1 = solution.fourSum(nums, target)
        result2 = solution.fourSumBrute(nums, target)
        print(nums, target, result1, result2, "\n")


def compare_lists(list1, list2):
    ''' Compare lists (will sort the lists)
    '''
    if type(list1) != type(list2):
        return False
    if isinstance(list1, list) and isinstance(list2, list):
        list1.sort()
        list2.sort()
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if not compare_lists(list1[i], list2[i]):
                return False
    else:
        if list1 != list2:
            return False
    return True


def random_test(runs):
    per_run = 10
    solution = Solution()
    for _ in range(runs):
        nums = [random.randint(-10, 10) for _ in range(10)]
        for _ in range(per_run):
            target = random.randint(-30, 30)
            result1 = solution.fourSum(nums, target)
            result2 = solution.fourSumBrute(nums, target)
            if not compare_lists(result1, result2):
                print(nums, target, result1, result2, "\n")
                return
    print(f"{runs * per_run} done, all ok")

if __name__ == "__main__":
    import random
    #main()
    random_test(1000)
