''' https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
'''

class Solution:
    def findArray(self, pref):

        result = [pref[0]]

        for i in range(1, len(pref)):
            result.append(pref[i] ^ pref[i-1])

        return result

def main():
    ''' Test findArray
    '''
    solution = Solution()

    test_cases = [
        [5,2,0,3,1],
        [13],
    ]
    for pref in test_cases:
        result = solution.findArray(pref)
        print(pref, result)

if __name__ == "__main__":
    main()