''' https://leetcode.com/problems/decoded-string-at-index/
'''

class Solution:
    def decodeAtIndex(self, s, k):

        # Work up to the moment k is included in the string
        log = []
        strlen = 0

        # log tracks the length of decoded string for each element of s
        for n, ch in enumerate(s):
            if ch in "abcdefghijklmnopqrstuvwxyz":
                strlen += 1
            else:
                strlen *= int(ch)
            log.append(strlen)
            if strlen >= k:
                s = s[:n+1]
                break

        # Now work it back until we match k

        for ch in s[::-1]:

            if ch in "abcdefghijklmnopqrstuvwxyz":
                if k == log[-1]:
                    return ch

            # Numbers, a bit tricky logic here
            else:
                # If k falls exactly on the end of the copy
                # Character should match the string before the copy
                if k == log[-1]:
                    k //= int(ch)
                # If k is somewhere before the copy
                # Then the size of copied chunk is log[-1]//int(ch)
                # And k should be modulo size of the chunk
                # Except chunksize, instead of 0
                elif k < log[-1]:
                    k %= log[-1]//int(ch)
                    if k == 0:
                        k = log[-1]//int(ch)

            log.pop()

        # Shouldn't come to this
        return ""

def main():
    ''' Test decodeAtIndex
    '''
    solution = Solution()

    test_cases = [
        ("leet2code3", 16), # o
        ("ha22", 8), # h
        ("a2345678999999999999999", 4), # a
        ("a5", 3),
    ]
    for s, k in test_cases:
        for i in range(1, k + 1):
            result = solution.decodeAtIndex(s, i)
            print(f"{s}, {i}, {result}")

if __name__ == "__main__":
    main()
