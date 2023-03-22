''' https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution():

    def longestPalindrome(self, s):
        # This is more of an "indented" solution, I guess -- it showed much
        # better results on the test cases. However, and this is where
        # I probably outsmarted myself, it performs kinda bad on strings
        # like "a"*1000, while my weird solutions with tokens shows more
        # decent results in that case.

        longest_pali = "" 

        # Go through all the potential centers of the pali
        for i in range(len(s)):
            
            # Initialization is a bit different for even and odd pali
            # But the rest is teh same, so we can combine it
            for mode in ("odd", "even"):

                # Odd pali starts from one character
                if mode == "odd":
                    left, right = i, i
                # Even - from adjacent characters
                elif mode == "even" and i > 0:
                    left, right = i - 1, i
                # No even palis in position 0
                else:
                    break

                while True:

                    # Exit if it is no longer a pali
                    if s[left] != s[right]:
                        break

                    # Update longest found pali
                    current_len = right - left + 1
                    current_pali = s[left: right + 1]
                    if current_len > len(longest_pali):
                        longest_pali = current_pali

                    # Try to expand
                    # Exit if the edge is found
                    if left - 1 < 0 or right + 1 > len(s) - 1:
                        break

                    left -= 1
                    right += 1

        return longest_pali


    def longestPalindrome_token(self, s):
        # This is the version I come up myself with. It is sort of O(n^3),
        # which is bad, but optimized with search tokens, so it was still
        # accepted, albeit with rather abysmal timing results.
        # It is actually not too bad if you consider
        # test cases like "a" * 1000 or "ab" * 500

        longest_pali = ""

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

            # Remaining string is shorter than longest pali we found
            if len(s) - i <= len(longest_pali):
                break

            # Generating straight tokens this time
            straight_token = s[i:i+token_size]

            # If straight token match a reverse token
            if straight_token in reversed_tokens:
                start = i

                # Go through all instances where reverse token was found
                for end in reversed_tokens[straight_token]:

                    # Token should be "facing" each other, otherwise ignore them
                    # Also if  potential pali is smaller than 2 tokens
                    # or smaller than the longest pali we already have
                    if end <= start or end - start < token_size * 2 or \
                        end - start <= len(longest_pali):
                        continue

                    # And check if this string is a pali
                    for shift in range((end - start) // 2):
                        if s[start + shift] != s[end - shift - 1]:
                            break
                    else:
                        # Keep track of the longest match
                        if end - start > len(longest_pali):
                            longest_pali = s[start:end]

        if longest_pali:
            return longest_pali

        # Part 2: Look for palis smaller than the token size

        # Go through all possible lengths of pali from the biggest to 2
        for length in range(token_size * 2, 1, -1):

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

    def longestPalindromeSlow(self, s):
        """ Original implementation.
        Slow, but I'll use it for automated testing
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
        "aabbbbbaaaaa",
        "aaaaaaaaaaaaaabaaaaaaaaaaaaa",
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
