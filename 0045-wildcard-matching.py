''' https://leetcode.com/problems/wildcard-matching/
'''

class Solution:

    def isMatch(self, s, p):

        #print(f"CALL: s='{s}', p='{p}'")

        # 1. Non-wild pattern

        # Split P into p_left, p_mid, p_right, where p_mid is
        # the first non-wild part of the pattern
        
        # First, find the boundaries of non-wild part
        non_wild_start, non_wild_end = None, None
        for pos, char in enumerate(p):
            if non_wild_start is None and char not in ("*", "?"):
                non_wild_start = pos
            if non_wild_start is not None and char in ("*", "?"):
                non_wild_end = pos
                break
            if non_wild_start is not None and pos == len(p)-1:
                non_wild_end = pos + 1

        # Non-wild pattern was found
        if non_wild_start is not None:

            # Break pattern by the first non-wild part
            p_left, p_mid, p_right = p[:non_wild_start], p[non_wild_start:non_wild_end], p[non_wild_end:]
            #print(f"1. '{p_left}', '{p_mid}', '{p_right}'")

            # Find possible splits in S by the same non-wild pattern

            for n in range(len(s) - len(p_mid) + 1):

                if s[n:n+len(p_mid)] == p_mid:
                    s_left, s_mid, s_right = s[:n], p_mid, s[n+len(p_mid):]
                    #print(f"1. found s split:, '{s_left}', '{s_mid}', '{s_right}'")

                    # Next step would be recursive comparison
                    if self.isMatch(s_left, p_left) and self.isMatch(s_right, p_right):
                        return True
            else:
                return False

        # 2. "?" Pattern

        # Find first "?" symbol in P
        q_pos = None
        for pos, char in enumerate(p):
            if char == "?":
                q_pos = pos
                break
        
        # ? was found
        if q_pos is not None:     

            # If it is one ? and one character in needle
            if p=="?" and len(s) == 1:
                #print("2. p==? len(s)==1")
                return True

            p_left, p_right = p[:q_pos], p[q_pos+1:]
            #print(f"2. '{p_left}', ?, '{p_right}'")
            
            # Split S at all letters (any can be an "?")
            for n in range(len(s)):
                s_left, s_right = s[:n], s[n+1:]
                #print(f"2. ? split:, '{s_left}', ?, '{s_right}'")

                # Next step would be recursive comparison
                if self.isMatch(s_left, p_left) and self.isMatch(s_right, p_right):
                    return True
            
            return False

        # 3. "*" Pattern

        # At this moment p is either empty or * (or multiple *, which doesn't matter)
        if s=="" and p=="":
            #print('3. s=="" and p=="", True')
            return True
        # * or multiple *s
        elif p=="*" or p!="" and p.count("*") == len(p):
            #print('3. p=="*", True')
            return True
        elif s!="" and p=="":
            #print('3. s!="" and p=="", False')
            return False

        # Should never reach this one

        return False

def main():
    ''' Test isMatch
    '''
    solution = Solution()

    test_cases = [
        ("aa", "a"),
        ("aa", "*"),
        ("cb", "?a"),
        ("cb", "c?"),
        ("saaaxxxbbbddccc", "?aaa???bbb**ccc"),
        ("daaxxxaaaddccc", "*?*aaa???bbb**ccc"),
        ("abc", "???"),
        ("ab", "???"),
        ("abcd", "???"),
        ("a", "*?"),
        ("ab", "*?b"),
        ("a", "?*"),
        ("a", "*?*"),
        ("a", "*??"),
        ("af", "?*?"),
        ("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
         "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"),
    ]
    for s, p in test_cases:
        start = time.time()
        result = solution.isMatch(s, p)
        elapsed = time.time() - start
        print(s[:50], p[:50], result, elapsed, "\n")

if __name__ == "__main__":
    import time

    main()
