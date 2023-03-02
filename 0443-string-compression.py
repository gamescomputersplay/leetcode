''' https://leetcode.com/problems/string-compression/
'''

class Solution:
    def compress(self, chars):

        return 0

def main():
    ''' Test compress
    '''
    solution = Solution()

    test_cases = [
        ["a","a","b","b","c","c","c"],
        ["a"],
        ["a","b","b","b","b","b","b","b","b","b","b","b","b"],

    ]
    for array in test_cases:
        array_original = array.copy()
        result = solution.compress(array)
        print("".join(array_original), "".join(array), result)



if __name__ == "__main__":
    main()
