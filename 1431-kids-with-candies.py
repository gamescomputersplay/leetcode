''' https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
'''

class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        # Resulting list
        is_new_max = []

        curr_max = max(candies)

        for candy in candies:
            
            if candy + extraCandies >= curr_max:
                is_new_max.append(True)
            else:
                is_new_max.append(False)

        return is_new_max
    
def main():
    ''' Test kidsWithCandies
    '''
    solution = Solution()

    test_cases = [
        ([2,3,5,1,3], 3),
        ([4,2,1,1,2], 1),
        ([12,1,12], 10),
    ]
    for candies, extraCandies in test_cases:
        result = solution.kidsWithCandies(candies, extraCandies)
        print(candies, extraCandies, result)



if __name__ == "__main__":
    main()
