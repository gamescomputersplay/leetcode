''' https://leetcode.com/problems/find-the-highest-altitude/
'''

class Solution:
    def largestAltitude(self, gain):

        max_hi = 0
        curr = 0
        
        for g in gain:
            curr += g
            max_hi = max(max_hi, curr)

        return max_hi

def main():
    ''' Test largestAltitude
    '''
    solution = Solution()

    test_cases = [
        [-5,1,5,0,-7],
        [-4,-3,-2,-1,4,3,2],
        [1, -2, 3, -4, 5, -6, -1, 2, 3, -4, 5, -6, 3], 
    ]
    for gain in test_cases:
        print()
        result = solution.largestAltitude(gain)
        print(gain, result)


if __name__ == "__main__":
    main()
