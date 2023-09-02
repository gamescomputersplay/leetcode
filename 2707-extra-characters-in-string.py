''' https://leetcode.com/problems/extra-characters-in-a-string
'''

class Solution:
    def minExtraChar(self, s, dictionary):

        can_start_here = [True] + [False] * (len(s)) 
        farthest_reached = 0
        removed = 0

        for pos in range(len(s)):

            if can_start_here[pos]:
                have_words = False
                for word in dictionary:
                    if s[pos:].startswith(word):
                        can_start_here[pos + len(word)] = True
                        farthest_reached = max(farthest_reached, pos + len(word))
                        have_words = True

                # No words are found and this is the farthest we gotten
                if not have_words and pos == farthest_reached:
                    removed += 1
                    farthest_reached += 1
                    can_start_here[pos + 1] = True

        # Add all False at the end of can_start_here
        while not can_start_here.pop():
            removed += 1

        return removed

def main():
    ''' Test minExtraChar
    '''
    solution = Solution()

    test_cases = [
        ("leetscodes", ["leet","code","leetcode"]),
        ("sayhellohellofworlda", ["hello","world"]),
        ("smsvy", ["y","m","s"]), #1
        ("metzeaencgpgvsckjrqafkxgyzbe", ["r","g","qafkx","t","jr","encgp","tze","yzbe","c","o","gv","at","x","ae"]), #5
    ]
    for s, dictionary in test_cases:

        result = solution.minExtraChar(s, dictionary)
        print(s, dictionary, result)

if __name__ == "__main__":
    main()
