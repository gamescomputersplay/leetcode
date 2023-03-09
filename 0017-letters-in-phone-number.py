''' https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

class Solution:
    def letterCombinations(self, digits):
        return []

def main():
    ''' test letterCombinations
    '''
    test_cases = [
        "23", # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        "", # []
        "2", # ["a","b","c"]
    ]

    solution = Solution()
    for digits in test_cases:
        print(digits, solution.letterCombinations(digits))


if __name__ == "__main__":
    main()