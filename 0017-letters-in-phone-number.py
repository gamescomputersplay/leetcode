''' https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

class Solution:
    def letterCombinations(self, digits):

        # Mapping to letters
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Start with "" to be able simply add letters
        current_result = [""]

        # Cycle through the digits
        for digit in digits:
            new_result = []

            # For each: look at all the permutations we had so far
            for permutation in current_result:

                # And add letters from the current digit
                for letter in letters[digit]:
                    new_result.append(permutation + letter)

            # Prepare results for the next cycle
            current_result = new_result

        # If it was an empty string, need to remove this one
        if "" in current_result:
            current_result.remove("")

        return current_result

def main():
    ''' test letterCombinations
    '''
    test_cases = [
        "23", # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        "", # []
        "2", # ["a","b","c"]
        "666",
        "277"
    ]

    solution = Solution()
    for digits in test_cases:
        print(digits, solution.letterCombinations(digits))


if __name__ == "__main__":
    main()