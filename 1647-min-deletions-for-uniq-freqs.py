''' https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
'''

class Solution:
    def minDeletions(self, s):

        freqs = {}
        for ch in s:
            freqs[ch] = freqs.get(ch, 0) + 1

        need_remove = 0
        prev_f = float("inf")

        for f in sorted(freqs.values(), reverse=True):

            if f >= prev_f:
                # Remove letter to end up "previous - 1",
                # but no more than there already is
                need_remove += min(f - prev_f + 1, f)
                # Which makes the f = pref_f - 1, but no lower than 0
                prev_f = max(prev_f - 1, 0)
            else:
                prev_f = f

        return need_remove

    
def main():
    ''' Test minDeletions
    '''
    solution = Solution()

    test_cases = [
        "aab",
        "aaabbbcc",
        "ceabaacb",
        "abcd",
        "a",
    ]
    for s in test_cases:
        result = solution.minDeletions(s)
        print(s, result)

if __name__ == "__main__":
    main()
        