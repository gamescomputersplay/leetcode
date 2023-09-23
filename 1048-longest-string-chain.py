''' https://leetcode.com/problems/longest-string-chain/
'''

class Solution:
    def longestStrChain(self, words):

        def is_step_away(w1, w2):

            p1, p2 = 0, 0
            while p1 < len(w1):
                if w1[p1] == w2[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p2 += 1
                    if p2 - p1 == 2:
                        return False
            return True


        # Split by word len and prepare place to track chain length
        # {len1: {"aaa": 2, "bbb": 3}}
        # Number is the longest chain up to this word

        lens = {}
        for word in words:
            if len(word) not in lens:
                lens[len(word)] = {}
            lens[len(word)][word] = 1
        #print(lens)

        word_lens = sorted(list(lens.keys()))
        max_len = 1

        for word_len in word_lens[:-1]:
            for word_from in lens[word_len].keys():
                if word_len + 1 in lens:
                    for word_to in lens[word_len + 1].keys():
                        if is_step_away(word_from, word_to):
                            lens[word_len + 1][word_to] = \
                                max(lens[word_len + 1][word_to], 
                                    lens[word_len][word_from] + 1)
                            max_len = max(max_len, lens[word_len + 1][word_to])

        return max_len

def main():
    ''' Test longestStrChain
    '''
    solution = Solution()

    test_cases = [
        ["a","b","ba","bca","bda","bdca"], # 4
        ["xbc","pcxbcf","xb","cxbc","pcxbc"], # 5
        ["abcd","dbqca"], # 1
        ["a","b","ab","bac"], # 2
    ]
    for words in test_cases:
        result = solution.longestStrChain(words)
        print(words, result)


if __name__ == "__main__":
    main()
        