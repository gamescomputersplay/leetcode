''' https://leetcode.com/problems/minimize-deviation-in-array/
'''

class Solution:
    def minimumDeviation(self, nums):
        
        # Set "variations" will contain all the options for each number
        # in the array, as tuples. For example, for [100, 1] it will be
        # {(100, 50, 25), (1, 2)}
        variations = set()
        for num in nums:

            if num % 2 == 1:
                variations.add((num * 2, num))
            else:
                evens = []
                while num % 2 == 0:
                    evens.append(num)
                    num //= 2
                evens.append(num)
                variations.add(tuple(evens))

        print(variations)

        # Check if there is a pair of min and max values
        # (not sure how explain this)
        hard_max = max((variation[-1] for variation in variations))
        hard_min = min((variation[0] for variation in variations))
        print(hard_max, hard_min)

        # Simple solution happens if:
        # 1. There is a valid hard_min - hard_max range
        # 2. All numbers have at least one variant in the range

        # Flag for a simple solution
        has_simple_solution = True

        # Let's compare our variations with the hard_min, hard_max
        for variation in variations:
            # If a variation has at least one number in the hard range
            for number in variation:
                if hard_min <= number <= hard_max:
                    break
            # But if it is not - no simple solution
            else:
                has_simple_solution = False
            if not has_simple_solution:
                break
        # Return simple solution if there is one
        else:
            return hard_max - hard_min

def main():
    ''' Test minimumDeviation
    '''
    solution = Solution()

    test_cases = [
        [1, 2, 3, 4],
        [4, 1, 5, 20, 3],
        [2, 10, 8],
        [100, 51],
        [100, 51, 103],
        [101, 120, 90]
    ]
    for array in test_cases:
        print()
        result = solution.minimumDeviation(array)
        print(array, result)



if __name__ == "__main__":
    main()
