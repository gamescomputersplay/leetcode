''' https://leetcode.com/problems/buddy-strings/
'''

class Solution:
    def buddyStrings(self, s, goal):

        # Different length - NO
        if len(s) != len(goal):
            return False

        # Different characters - NO
        if sorted(list(s)) != sorted(list(goal)):
            return False

        # Same strings - NO if all characters present only once
        if s == goal:
            for ch in set(s):
                if s.count(ch) > 1:
                    return True
            return False

        # If there are exactly 2 mismatches - YES
        count_mismatches = 0
        for pos, ch in enumerate(s):
            if goal[pos] != ch:
                count_mismatches += 1

        return count_mismatches == 2


def main():
    ''' Test buddyStrings
    '''
    solution = Solution()

    test_cases = [
        ("ab", "ba"),
        ("ab", "ab"),
        ("aa", "aa"),
        ("abcdefghijk", "abidefghjck"),
    ]
    for s, goal in test_cases:
        result = solution.buddyStrings(s, goal)
        print(f"{s}, {goal}, {result}")

if __name__ == "__main__":
    main()