''' https://leetcode.com/problems/extra-characters-in-a-string
'''

class Solution:
    def minExtraChar(self, s, dictionary):

        # How many skips you need to start from this position
        need_skips = [0] + [float("inf")] * (len(s)) 

        for pos in range(len(s) + 1):

            need_skips[pos] = min(need_skips[pos], need_skips[pos - 1] + 1)

            for word in dictionary:

                if s[pos:].startswith(word):
                    need_skips[pos + len(word)] = min(need_skips[pos], need_skips[pos + len(word)])

        end_nones = 0
        while need_skips[-1] == float("inf"):
            need_skips.pop()
            end_nones += 1

        return need_skips[-1] + end_nones

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
