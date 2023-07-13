''' https://leetcode.com/problems/edit-distance/
'''

class Solution:

    def __init__(self):
        self.cache = {}

    def minDistance(self, word1, word2):

        def tokenize(word):
            tokens = set()
            for token_size in range(1, len(word) + 1):
                for n in range(len(word) - token_size + 1):
                    tokens.add(word[n:n+token_size])
            return tokens

        def find_tokens(word1, word2):
            tokens1 = tokenize(word1)
            tokens2 = tokenize(word2)
            tokens = tokens1.intersection(tokens2)
            if tokens:
                return tokens
            return None

        key = word1 + " " + word2
        if key in self.cache:
            return self.cache[key]

        if word1 == "":
            self.cache[key] = len(word2)
            return self.cache[key]
        if word2 == "":
            self.cache[key] = len(word1)     
            return self.cache[key]

        if len(word1) == 1 and len(word2) == 1:
            self.cache[key] = 1 if word1[0] != word2[0] else 0
            return self.cache[key]

        # Find matching bits
        tokens = find_tokens(word1, word2)

        # No matches at all
        if not tokens:
            self.cache[key] = max(len(word1), len(word2))
            return self.cache[key]

        best_result = float("inf")
        for token in tokens:

            splits1 = [i for i in range(len(word1)) if word1.startswith(token, i)]
            splits2 = [i for i in range(len(word2)) if word2.startswith(token, i)]

            for split1 in splits1:
                for split2 in splits2:

                    beg1, end1 = word1[:split1], word1[split1+len(token):]
                    beg2, end2 = word2[:split2], word2[split2+len(token):]

                    best_result = min(best_result, self.minDistance(beg1, beg2)
                                      + self.minDistance(end1, end2))

        # Whatever we have calculated there, it sould not be bigger
        # than just replacing all letters (whilch is maxlen of either word)
        best_result = min(best_result, max(len(word1), len(word2)))

        self.cache[key] = best_result
        return self.cache[key]

def large_case():
    word1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef"
    word2 = "bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"
    solution = Solution()
    start = time.time()
    result = solution.minDistance(word1, word2)
    elapsed = time.time() - start
    print(f"Solution: {solution}")
    print(f"Elapsed: {elapsed}s")

def main():
    ''' Test minDistance
    '''
    solution = Solution()

    test_cases = [
        ("horse", "ros"), #3
        ("intention", "execution"), #5
        ("moscow", "washington"), #8
        ("plasma", "altruism"), #6
        ("a", "a"), #0
        ("abcdxabcde", "abcdeabcdx"), #2
        ("teacher", "botcher"), #3
        ("tea", "bot")
    ]

    for word1, word2 in test_cases:
        result = solution.minDistance(word1, word2)
        print(word1, word2, result)

if __name__ == "__main__":
    import time
    main()
    large_case()
