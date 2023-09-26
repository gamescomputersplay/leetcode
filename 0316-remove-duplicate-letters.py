''' https://leetcode.com/problems/remove-duplicate-letters/
'''

class Solution:
    def removeDuplicateLetters(self, s):

        # No changes for 1-letter string
        if len(s) == 1:
            return s

        # Calculate letters' frrquencies
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        string = list(s)

        # Pointers to go through the original string
        p_left, p_right = 0, 1

        while p_right < len(s):

            # Delete repeated character
            if string[p_left] == string[p_right]:
                freq[string[p_left]] -= 1
                string[p_right] = ""
                p_right += 1

            # Right order - do nothing, go to the next one
            elif string[p_left] < string[p_right]:
                p_left = p_right
                p_right += 1

            # Wrong order
            elif string[p_left] > string[p_right]:
                # Delete left character if we can
                if freq[string[p_left]] > 1:
                    freq[string[p_left]] -= 1
                    string[p_left] = ""
                    while p_left >= 0 and string[p_left] == "":
                        p_left -= 1
                    if p_left == -1:
                        p_left = p_right
                        p_right += 1
                # Or just move on
                else:
                    p_left = p_right
                    p_right += 1

        # Delete remaining duplicates
        for pos in range(len(s)-1, -1, -1):
            if string[pos] != "" and freq[string[pos]] > 1:
                freq[string[pos]] -= 1
                string[pos] = ""

        return "".join(string)

    def removeDuplicateLettersSlow(self, s):
        ''' Slow but surer way, to check validity
        '''
        s = list(s)
        while True:
            for pos in range(len(s)-2, -1, -1):
                if s[pos] >= s[pos + 1] and s.count(s[pos]) > 1:
                    del s[pos]
                    break
            else:
                break

        while True:
            for pos in range(len(s)-1, -1, -1):
                if s.count(s[pos]) > 1:
                    del s[pos]
                    break
            else:
                break

        return "".join(s)

def main():
    ''' Test removeDuplicateLetters
    '''
    solution = Solution()

    test_cases = [
        # "bcabc",
        # "cbacdcbc",
        # "dddeffsbbbbaaebabbsf",
        "abacb",
    ]

    for s in test_cases:
        result = solution.removeDuplicateLetters(s)
        result2 = solution.removeDuplicateLettersSlow(s)
        print(s, result, result == result2)

def random_test(runs):
    solution = Solution()
    for _ in range(runs):
        s = random.choices("abcdefg", k=10)
        result = solution.removeDuplicateLetters(s)
        result2 = solution.removeDuplicateLettersSlow(s)
        if result != result2:
            print(f"Failed on {testcase}: {result} != {result2}")
            return
    print(f"{runs} random tests okay")     


if __name__ == "__main__":
    import random
    main()
    # random_test(10000)
        