''' https://leetcode.com/problems/valid-palindrome/
'''

class Solution:
    def isPalindrome(self, s):
        sfix = ""
        for ch in s.lower():
            if ch in "abcdefghijklmnopqrstuvwxyz1234567890":
                sfix += ch
        for i in range(len(sfix)//2):
            if sfix[i] != sfix[-i-1]:
                return False
        return True

def main():
    ''' Test isPalindrome
    '''
    solution = Solution()

    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "test s tset",
        " ",
        "ab",
        "Fb Ley'?P:\"'I\":P?IyeL bF",
    ]
    for nums in test_cases:
        result = solution.isPalindrome(nums)
        print(nums, result)


if __name__ == "__main__":
    main()

