''' https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
'''

class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):

        max_conseq = 1

        # Do it twice, second time reversing the T and F
        for F, T in (("F", "T"), ("T", "F")):

            start = 0 # First character in the window 
            end = 1 # First character after the window
            made_switches = 1 if answerKey[0] == F else 0

            while True:

                # Done if have reached the end of the string
                if end == len(answerKey):
                    break

                # Keep growing the window while we can (next is "T")
                if answerKey[end] == T:
                    end += 1
                    max_conseq = max(max_conseq, end - start)

                # We found an "F"
                # But we can still change it
                elif made_switches < k:
                    end += 1
                    made_switches += 1
                    max_conseq = max(max_conseq, end - start)

                # We can't switch anymore, need to pull the start first
                else:
                    # Start should be on the first F in window
                    while answerKey[start] != F:
                        start += 1

                    # Than start moves to the right
                    start += 1
                    end += 1
                    max_conseq = max(max_conseq, end - start)

        return max_conseq

def main():
    ''' Test getAverages
    '''
    solution = Solution()

    test_cases = [
        ("TTFF", 2),
        ("TFFT", 1),
        ("TTFTTFTT", 1),
        ("TF", 1),
    ]
    for answerKey, k in test_cases:
        result = solution.maxConsecutiveAnswers(answerKey, k)
        print(answerKey, k, result)

if __name__ == "__main__":
    main()
