''' https://leetcode.com/problems/median-of-two-sorted-arrays/
'''


class Solution(object):
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def regular_median(array):
            ''' Return a median of a sorted array
            '''
            if len(array) % 2 == 0:
                return (array[len(array) // 2] + array[(len(array) // 2) - 1]) / 2
            return float(array[len(array) // 2])

        def edges(keep1):
            ''' If first "keep_left" elements from the nums1 list go to
            the smaller half, in the final left half, what would be
            max and min elements of resulting arrays
            Return {left1}, {left2}), ({right1}, {right2}
            '''

            # This is how many elements should go to the right part
            keep2 = total_count // 2 - keep1

            # print()
            # print(keep_left, keep_right)
            # print(keep1, ":", nums1[:keep1] , nums2[:keep2], 
            #    "|", nums1[keep1:], nums2[keep2:])

            # Calculate max values for keep (left) parts
            left1 = nums1[keep1-1] if keep1 > 0 else None
            left2 = nums2[keep2-1] if keep2 > 0 else None

            # and max values of no-keep (right) parts
            right1 = nums1[keep1] if keep1 < len(nums1) else None
            right2 = nums2[keep2] if keep2 < len(nums2) else None


            # print(f"({left1}, {left2}), ({right1}, {right2})")
            return left1, left2, right1, right2


        # Sanitizing: one of the inputs is empty
        # (assuming that at least one of them isn't)
        if not nums1:
            return regular_median(nums2)
        if not nums2:
            return regular_median(nums1)

        # We want nums1 to be the longer of the two
        # Swap them if it is not the case
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        total_count = len(nums1) + len(nums2)


        # Bottom and top is the range of possible keep1 values
        # We'll do binary search within this range
        bottom = total_count // 2 - len(nums2)
        top = total_count // 2 + 1

        while True:

            # Number (of elements to be on the left in the nums1) to test
            middle = (top + bottom) // 2
            # print(f"\nItems in nums1: Left {bottom}, Right {top}, Middle {middle}")

            # Resulting min and max values of teh divided halves
            max_left1, max_left2, min_right1, min_right2 = edges(middle)
            # print(f"({max_left1}, {max_left2}), ({min_right1}, {min_right2})")              

            # Min and Max of of both parts (ignore None while comparing)
            max_left = max([val for val in (max_left1, max_left2) if val is not None])
            min_right = min([val for val in (min_right1, min_right2) if val is not None])

            # print(max_left, min_right)

            if max_left <= min_right:
                #print("Found")
                break

            # Depending of which part sticks out, adjust binary interval
            if max_left1 > min_right2:
                top = middle
            if max_left2 > min_right1:
                bottom = middle

        # Even: median in in between two lists
        if total_count % 2 == 0:
            return (max_left + min_right) / 2
        # Odd: Minimum element on the right is the median
        return float(min_right)

def brute_median(list1, list2):
    ''' Very simple way of solving the same problem.
    Destructive to list1, but it's okay, we'll launch it last.
    '''
    list1.extend(list2)
    list1.sort()
    if len(list1) % 2 == 0:
        return (list1[len(list1) // 2] + list1[(len(list1) // 2) - 1]) / 2
    return float(list1[len(list1) // 2])

def run_testcases(test_cases):
    ''' Manual test of findMedianSortedArrays
    '''
    solution = Solution()

    for list1, list2 in test_cases:
        # print(list1, list2)
        result = solution.findMedianSortedArrays(list1, list2)
        result_correct = result == brute_median(list1, list2)
        print(result, result_correct)

def generate_testcases(cases_to_generate):
    ''' Randomly generated test cases
    '''
    def random_list(length, spread):
        ''' Generate a random list
        '''
        return [random.randint(0, spread) for num in range(length)]

    cases = []

    while len(cases) < cases_to_generate:
        list1 = random_list(random.randint(0, 10), random.randint(0, 10))
        list2 = random_list(random.randint(0, 10), random.randint(0, 10))

        if list1 or list2:
            cases.append((list1, list2))

    return cases

if __name__ == "__main__":

    import random 
    random.seed(0)
    test_cases = [
        ([3], []), # 3
        ([1, 3, 5], []), # 3
        ([], [1, 2, 3, 4]), # 2.5
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), # 1
        ([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]), # 1.5
        ([1, 1, 1, 1, 1], [2, 2, 2, 2]), # 1
        ([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12]), # 6.5
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8]), # 7.5
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], [2, 4, 6, 8]), # 7.0
        ([1], [2]), # 1.5
        ([1, 3], [2]), # 2
        ([1, 2], [3, 4]), # 2.5
        ([1, 2, 3, 4], [5, 6, 7, 8]), # 5.5
    ]
    #run_testcases(test_cases)

    random_cases = generate_testcases(10)
    print(random_cases)
    run_testcases(random_cases)
