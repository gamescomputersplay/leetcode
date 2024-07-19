''' https://leetcode.com/problems/largest-number/
'''

class Solution:
    def largestNumber(self, nums):

        def compare(num1, num2):
            ''' Compare 2 string numbers
            Returns:
                1 - if num1 is bigger
                -1 - if num2 is bigger
                0 - if the same or inconclusive ("90" and "9")
            '''
            for pos in range(min(len(num1), len(num2))):
                if num1[pos] > num2[pos]:
                    return 1
                if num1[pos] < num2[pos]:
                    return -1
            return 0

        def get_largest_recursively(nums_now, string_now):
            nonlocal largest_so_far

            highest_new_num = "0"

            for n, new_num in enumerate(nums_now):

                number_is_high = compare(highest_new_num, new_num)

                if number_is_high == -1:
                    highest_new_num = new_num
                if number_is_high == 1:
                    break

                new_string = string_now + new_num

                # New option is worth than we have so far
                compare_to_largest = compare(largest_so_far + "0", new_string)
                if compare_to_largest == 1:
                    continue

                if compare_to_largest == -1:
                    largest_so_far = new_string

                new_nums = nums_now.copy()
                del new_nums[n]
                get_largest_recursively(new_nums, new_string)

        nums = [str(n) for n in nums]
        maxlen = max(len(s) for s in nums)
        nums.sort(key=lambda x: x + "9" * (maxlen-len(x)), reverse=True)

        largest_so_far = ""
        #get_largest_recursively(nums, "")
        return "".join(nums)
        return largest_so_far

def main():
    ''' Test largestNumber
    '''
    solution = Solution()

    test_cases = [
        [10, 2],
        [3,30,34,5,9],
        [9995, 99, 9, 9998],
        [9,9,9,9],
    ]
    for nums in test_cases:
        result = solution.largestNumber(nums)
        print(nums, result)

def test_with_timing():
    import time

    solution = Solution()
    nums = [i for i in range(1, 101)]

    start = time.time()
    result = solution.largestNumber(nums)
    duration = time.time() - start
    print(nums, result, f"t={duration}")
    print(result=="999989796959493929190898888786858483828180797877776757473727170696867666656463626160595857565555453525150494847464544443424140393837363534333323130292827262524232222120191817161514131211110100")

if __name__ == "__main__":
    main()
    test_with_timing()
