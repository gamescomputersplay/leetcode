''' https://leetcode.com/problems/palindrome-partitioning-ii/
'''

class Solution:
    def minCut(self, s):

        def find_longest_pali_in_substring(beg, end):

            if beg == end:
                return [(beg, end)]

            longest_pali_coords = {}

            for start in range(beg, end):

                for mode in ("odd", "even"):

                    if mode == "odd":
                        i, j = start, start
                    else:
                        i, j = start, start + 1

                    while True:
                        if i<beg or j>end or s[i] != s[j]:
                            break
                        if j-i + 1 > 1:
                            if j-i + 1 not in longest_pali_coords:
                                longest_pali_coords[j-i + 1] = []
                            longest_pali_coords[j-i + 1].append((i, j))
                        i -= 1
                        j += 1

            if not longest_pali_coords:
                return [(beg, beg)]

            lengths = sorted(list(longest_pali_coords.keys()))

            good_enough_palis = []
            for length in lengths[-4:]:
                good_enough_palis += longest_pali_coords[length]
            return good_enough_palis

        def count_cuts_rec(beg, end):

            if (beg, end) in cache_cuts:
                return cache_cuts[(beg, end)]

            cuts = []
            longest_pali_coords = find_longest_pali_in_substring(beg, end)

            for left, right in longest_pali_coords:

                cuts.append(0)
                if left != beg:
                    cuts[-1] += 1 + count_cuts_rec(beg, left-1)
                if right != end:
                    cuts[-1] += 1 + count_cuts_rec(right + 1, end)

            cache_cuts[(beg, end)] = min(cuts)
            return cache_cuts[(beg, end)]

        cache_cuts = {}

        return count_cuts_rec(0, len(s)-1)


    def minCut_brute_force(self, s):

        def is_pali(string):
            for i in range(len(string)//2):
                if string[i] != string[-1-i]:
                    return False
            return True

        def partition_remaining_string(start_with):
            ''' Do the partitioning for segment starting from "start_with"
            '''

            if len(s) - start_with == 1:
                return [[s[start_with]]]

            result = []

            # Also check if full string is a pali and include if it is
            if is_pali(s[start_with:]):
                result.append([s[start_with:]])

            # Check all possible lengths starting from the beginning
            for word_len in range(1, len(s) - start_with):

                # Skip non-palis
                word = s[start_with:start_with+word_len]
                if not is_pali(word):
                    continue

                # Check what the options for the remainder of teh string would be
                options = partition_remaining_string(start_with + word_len)

                # Combine them with the word
                for option in options:
                    new_option = [word]
                    new_option.extend(option)
                    result.append(new_option)

            return result

        partitions = partition_remaining_string(0)
        return min(len(partition) for partition in partitions) - 1

def main():
    ''' Test minCut
    '''
    solution = Solution()

    test_cases = [
        "aab",
        "a",
        "ab",
        "aabbccdbbsaasc",
        "abcabckjhaaabcbcbaaacbacbasd",
        "abcabkkkfkkkfkkkfkkkckjhaaabcbcbaaacbacbasd",
        "aababc", #2
        # exp 452
        "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp",
        # exp 273
        "adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece",
        # exp 1
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "abaaaaabba", #2
        # exp 13
        "bbaababaabaabaaababbabaabbaaababaaabababaabaababbbaaaaaabbabaababbabaaababbabbbaaaaaaba"

    ]
    for s in test_cases:
        result = solution.minCut(s)
        result_bf = 0
        #result_bf = solution.minCut_brute_force(s)
        print(s, result, result == result_bf)


if __name__ == "__main__":
    main()
