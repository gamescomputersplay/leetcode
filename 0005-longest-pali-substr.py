''' https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution():
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Part 1: fast string search based on tokens

        token_size = 4
        # We'll keep them in the dictionary as {"token": position,}
        reversed_tokens = {}

        reversed_string = s[::-1]

        # Generate dict of reversed tokens
        for i in range(len(reversed_string) - token_size + 1):

            # if token present several times, keep all it's positions
            reversed_token = reversed_string[i:i+token_size]
            if reversed_token not in reversed_tokens:
                reversed_tokens[reversed_token] = [len(reversed_string)-i]
            else:
                reversed_tokens[reversed_token].append(len(reversed_string)-i)

        # Go through the string again
        for i in range(len(s) - token_size + 1):
            # Generating straight tokens this time
            straight_token = s[i:i+token_size]

            # If straight token match a reverse token
            if straight_token in reversed_tokens:
                start = i

                # Go through all instances where reverse token was found
                for end in reversed_tokens[straight_token]:

                    # Token should be "facing" each other, otherwise ignore them
                    if end <= start:
                        continue

                    # And check if this string is a pali
                    for shift in range((end - start) // 2):
                        if s[start + shift] != s[end - shift - 1]:
                            break
                    else:
                        # Return the first found one (it should be the longest)
                        return s[start:end]

        # Part 2: Look for palis smaller than the token size

        # Go through all possible lengths of pali from the biggest to 2
        for length in range(token_size, 1, -1):

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
        "a",
        "bb",
        "babad", # "bab" or "aba"
        "cbbd", # bb
        "a" * 1000,
        "ab" * 500,
        "abcd" * 250 + "d",
        "abcdefghijklmnopabbarstuvdcbawxyz",
        "abcdefghijklmnopqdcbarstuvwxyz",
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
