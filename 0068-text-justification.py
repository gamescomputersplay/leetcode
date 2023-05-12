''' https://leetcode.com/problems/text-justification/
'''

class Solution:
    def fullJustify(self, words, maxWidth):

        # Step 1. Break words into lines
        lines = [[]]
        line_use_counter = 0
        for word in words:
            if len(word) <= maxWidth - line_use_counter:
                lines[-1].append(word)
                line_use_counter += len(word) + 1
            else:
                lines.append([word])
                line_use_counter = len(word) + 1

        # Step 2. Calculate spaces

        result = []

        for line_n, line in enumerate(lines):

            # left aligned last line
            if line_n == len(lines) - 1:
                result_line = " ".join(line).ljust(maxWidth)
            # left aligned line with one word
            elif len(line) == 1:
                result_line = line[0].ljust(maxWidth)

            else:
                need_spaces = maxWidth - sum(len(word) for word in line)
                base_space = need_spaces // (len(line) - 1)
                extra_spaces = need_spaces % (len(line) - 1)

                if extra_spaces > 0:

                    result_line = (" " * (base_space + 1)).join(line[:extra_spaces+1]) + " " * base_space
                    result_line += (" " * base_space).join(line[extra_spaces+1:])
                else:
                    result_line = (" " * base_space).join(line)

            result.append(result_line)

        return result
    
def main(verbose=True):
    ''' Test fullJustify
    '''
    solution = Solution()

    test_cases = [
        (["a", "bbbbbbbbb"], 10),
        (["This", "is", "an", "example", "of", "text", "justification."], 16),
        (["What","must","be","acknowledgment","shall","be"],  16),
        (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20),
    ]

    for words, maxWidth in test_cases:
        result = solution.fullJustify(words, maxWidth)
        if verbose:
            for line in result:
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