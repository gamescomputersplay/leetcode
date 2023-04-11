''' https://leetcode.com/problems/removing-stars-from-a-string/
'''

class Solution:
    def removeStars(self, s):

        result = []

        for char in s:

            if char == "*":
                result.pop()
            else:
                result.append(char)

        return "".join(result)

def main():
    ''' Test removeStars
    '''
    solution = Solution()

    test_cases = [
        "leet**cod*e",
        "erase*****",
        "a",
    ]
    for string in test_cases:

        result = solution.removeStars(string)
        print(string, result)


if __name__ == "__main__":
    main()
