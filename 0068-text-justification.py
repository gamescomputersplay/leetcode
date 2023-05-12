''' https://leetcode.com/problems/text-justification/
'''

class Solution:
    def fullJustify(self, words, maxWidth):
        return []
    
def main(verbose=True):
    ''' Test fullJustify
    '''
    solution = Solution()

    test_cases = [
       (["This", "is", "an", "example", "of", "text", "justification."], 16),
       (["What","must","be","acknowledgment","shall","be"],  16),
       (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20),
    ]

    for words, maxWidth in test_cases:
        result = solution.fullJustify(words, maxWidth)
        if verbose:
            for lin in result:
                print(f"'{line}'")
            print()

def test_timing(runs=1000):

    start = time.time()
    for _ in range(runs):
        main(verbose=False)
    elapsed = time.time() - start
    print(elapsed)

if __name__ == "__main__":
    import time
    main()
    test_timing()