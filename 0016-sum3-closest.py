''' https://leetcode.com/problems/3sum-closest/
'''

class Solution:
    def threeSumClosest(self, nums, target):

        def compare(single, pair):
            nonlocal minimal_distance, sum_when_minimal_difference
            # Make sure we have 3 distinct positions
            if single[1] == pair[1] or single[1] == pair[2]:
                return None
            if abs(single[0] - pair[0]) < minimal_distance:
                minimal_distance = abs(single[0] - pair[0])
                sum_when_minimal_difference = nums[single[1]] + nums[pair[1]] + nums[pair[2]]
            return None

        # Generate a list of "- sums - target" of all pairs, as:
        # [(-sum, position1, position2), ...]
        pair_sums = []
        for position_1, num_1 in enumerate(nums):
            for position_2, num_2 in enumerate(nums[:position_1]):
                pair_sums.append((target - num_1 - num_2, position_1, position_2))

        # Another list is a list of sigle values as [(val, position, None)]
        single_values = [(val, position, None) for position, val in enumerate(nums)]

        # Combine and sort two lists
        combined = pair_sums + single_values

        # Sort by the first value in a tuple (that is target-pair and values)
        combined.sort(key=lambda x: x[0])
        #print(combined)

        # Next we use the fact that the closer equation val3 ~ target-val1 - val2,
        # the closer target ~ val1 + val2 + val3 is too

        minimal_distance = float("inf")
        sum_when_minimal_difference = None

        for position, element in enumerate(combined):

            # Do the comparison only for Single elements
            if element[2] is not None:
                continue
            
            # Find a pair to the right, made with different numbers
            right = position + 1
            while right < len(combined) and combined[right][2] is None and \
                  position not in combined[right][1:]:
                  right += 1

            if right < len(combined):
                compare(element, combined[right])


        return sum_when_minimal_difference


    def threeSumClosestBrute(self, nums, target):
        ''' Same with BruteForce
        '''

        min_dist = float("inf")
        sum_when_min_dist = None

        for i, num_1 in enumerate(nums):
            for j, num_2 in enumerate(nums):
                for k, num_3 in enumerate(nums):

                    if i != j and j!= k and k != i:
                        dist = abs(target - num_1 - num_2 - num_3)
                        if dist < min_dist:
                            min_dist = dist
                            sum_when_min_dist = num_1 + num_2 + num_3
        return sum_when_min_dist


def main():
    ''' Test threeSumClosest
    '''
    solution = Solution()

    test_cases = [
        ([1, 1, 1, 1, 1, 1, 2], 20),
        ([891, 396, -546, 484, -525, 301, -867, 64, -341, -904], 3509),
        #([-1, 2, 1, -4], 1), #2
        #([0, 0, 0], 1), #0
    ]
    for nums, target in test_cases:
        result = solution.threeSumClosest(nums, target)
        result2 = solution.threeSumClosestBrute(nums, target)
        print(nums, target, result, result2)

def test_random(cases):
    solution = Solution()
    for _ in range(cases):
        nums = [random.randint(-1000, 1000) for _ in range(10)]
        target = random.randint(-10000, 10000)
        result = solution.threeSumClosest(nums, target)
        result2 = solution.threeSumClosestBrute(nums, target)
        if result != result2:
            print(f"Error in case: {nums}, {target}")
            print(f"Answers were {result} and {result2}")
            return
    print(f"{cases} done, all okay")

def large_case(case_size):
    ''' Time the large case
    '''
    nums = [random.randint(-10000, 10000) for i in range(case_size)]
    target = random.randint(-10000, 10000)
    solution = Solution()
    start = time.time()
    solution.threeSumClosest(nums, target)
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
    #test_random(10)
    #test_timing()
