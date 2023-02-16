''' https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Go through all possible lengths of pali from the biggest to 2
        for length in range(len(s), 1, -1):

            # Go through all positions where pali of that length can occur
            for start in range(0, len(s) - length + 1):

                # From out in, go through pair of letters
                for position in range(0, length // 2):
                    
                    # If letters are not the same - this is not
                    # a pali, next position
                    if s[start + position] != s[start + length - position - 1]:
                        break

                # If there was no mismatch - it is a pali, return it!
                else:
                    return s[start:start+length]

        # If no pali is found, return the first letter
        return s[0]


def main():
    ''' Test longestPalindrome
    '''
    solution = Solution()

    test_cases = [
        #"a",
        #"bb",
        #"babad", # "bab" or "aba"
        #"cbbd", # bb
        #"a" * 1000,
        #"ab" * 500,
        #"abcd" * 250 + "d",
        "glwhcebdjbdroiurzfxxrbhzibilmcfasshhtyngwrsnbdpzgjphujzuawbebyhvxfhtoozcitaqibvvowyluvdbvoqikgojxcefzpdgahujuxpiclrrmalncdrotsgkpnfyujgvmhydrzdpiudkfchtklsaprptkzhwxsgafsvkahkbsighlyhjvbburdfjdfvjbaiivqxdqwivsjzztzkzygcsyxlvvwlckbsmvwjvrhvqfewjxgefeowfhrcturolvfgxilqdqvitbcebuooclugypurlsbdfquzsqngbscqwlrdpxeahricvtfqpnrfwbyjvahrtosovsbzhxtutyfjwjbpkfujeoueykmbcjtluuxvmffwgqjgrtsxtdimsescgahnudmsmyfijtfrcbkibbypenxnpiozzrnljazjgrftitldcueswqitrcvjzvlhionutppppzxoepvtzhkzjetpfqsuirdcyqfjsqhdewswldawhdyijhpqtrwgyfmmyhhkrafisicstqxokdmynnnqxaekzcgygsuzfiguujyxowqdfylesbzhnpznayzlinerzdqjrylyfzndgqokovabhzuskwozuxcsmyclvfwkbimhkdmjacesnvorrrvdwcgfewchbsyzrkktsjxgyybgwbvktvxyurufsrdufcunnfswqddukqrxyrueienhccpeuqbkbumlpxnudmwqdkzvsqsozkifpznwapxaxdclxjxuciyulsbxvwdoiolgxkhlrytiwrpvtjdwsssahupoyyjveedgqsthefdyxvjweaimadykubntfqcpbjyqbtnunuxzyytxfedrycsdhkfymaykeubowvkszzwmbbjezrphqildkmllskfawmcohdqalgccffxursvbyikjoglnillapcbcjuhaxukfhalcslemluvornmijbeawxzokgnlzugxkshrpojrwaasgfmjvkghpdyxt",
    ]

    for string  in test_cases:
        start = time.time()
        result = solution.longestPalindrome(string)
        timing = time.time() - start
        print()
        print(string[:10], "..." if len(string) > 10 else "")
        print(result)
        print(f"Done in {timing}")

if __name__ == "__main__":
    import time
    main()
