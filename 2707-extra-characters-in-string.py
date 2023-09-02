''' https://leetcode.com/problems/extra-characters-in-a-string
'''

class Solution:
    def minExtraChar(self, s, dictionary):

        # How many skips you need to start from this position
        need_skips = [0] + [float("inf")] * (len(s)) 

        # Go through all positions
        for pos in range(len(s) + 1):

            # Either there was a way to get here or
            # skip from the previous one - whichever is ffaster
            need_skips[pos] = min(need_skips[pos], need_skips[pos - 1] + 1)

            # Any words match?
            for word in dictionary:

                # If so, mark the spot where the word ends as having
                # the same number of skips as this position
                # (but only overwrite if it is smaller)
                if s[pos:pos + len(word)] == word:
                    need_skips[pos + len(word)] = min(need_skips[pos], need_skips[pos + len(word)])

        return need_skips[-1]

def main():
    ''' Test minExtraChar
    '''
    solution = Solution()

    test_cases = [
        ("leetscodes", ["leet","code","leetcode"]),
        ("sayhellohellofworlda", ["hello","world"]),
        ("smsvy", ["y","m","s"]), #1
        ("metzeaencgpgvsckjrqafkxgyzbe",
        ["r","g","qafkx","t","jr","encgp","tze","yzbe","c","o","gv","at","x","ae"]), #5
        ("kpqcavgyrvihakwwsa",
        ["sa","ca","r","yrvi","wws"]), #9
    ]
    for s, dictionary in test_cases:

        result = solution.minExtraChar(s, dictionary)
        print(s, dictionary, result)

if __name__ == "__main__":
    main()
