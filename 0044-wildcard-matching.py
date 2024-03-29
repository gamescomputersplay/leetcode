''' https://leetcode.com/problems/wildcard-matching/
'''

class Solution:

    def isMatch(self, s, p):

        # Keep track of the position to return to:
        # (position of "*" in pattern, position of the first character to match in string)
        backtrack_log = []

        s_pointer = 0
        p_pointer = 0

        while True:

            # try:
            #     print(s_pointer, p_pointer, s[s_pointer], p[p_pointer], backtrack_log)
            # except:
            #     print(s_pointer, p_pointer, backtrack_log)

            # Both reached the end at the same time, matching successful
            if p_pointer == len(p) and s_pointer == len(s):
                return True
            
            # End of S, but P is on "*", skip "*"
            elif s_pointer == len(s) and p[p_pointer] == "*" :
                pass

            # Match failed:
            # - either reached the end not at the same time, 
            # - or non-wild character doesn't match
            # Need to go back to the last back tracking position
            elif p_pointer == len(p) and s_pointer != len(s) or \
                 p_pointer != len(p) and s_pointer == len(s) or \
                 p[p_pointer] not in ("*", "?") and p[p_pointer] != s[s_pointer]:
                
                # No backtracking to return to: Matching fail
                if not backtrack_log:
                    return False
                
                # Restore the backtracking position
                s_pointer, p_pointer = backtrack_log.pop()
                # But with S one place to the right
                s_pointer += 1

                # If there is no more S to go
                if s_pointer == len(s):
                    # There is nothing after * anyway
                    if p_pointer == len(p) - 1:
                        return True
                    # But if there is
                    return False
                
                # Save the updated backtracking info
                backtrack_log.append((s_pointer, p_pointer))

 
            # S and P have the same symbol or P has "?"
            elif p[p_pointer] == s[s_pointer] or p[p_pointer] =="?":
                s_pointer += 1

            # P has "*"
            elif p[p_pointer] =="*":
                # Set up a new point for backtracking
                backtrack_log.append((s_pointer, p_pointer))
            
            # Next character in P
            p_pointer += 1

        # Shouldn't reach this
        return False




    # First version, based on looking for non-wild parts and
    # recursively checking parts around them

    def __init__(self):
        self.cache = {}

    def isMatch_v1(self, s, p):

        if (s, p) in self.cache:
            return self.cache[(s, p)]

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
                    if self.isMatch_v1(s_left, p_left) and self.isMatch_v1(s_right, p_right):
                        self.cache[(s, p)] = True
                        return True
            else:
                self.cache[(s, p)] = False
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
                self.cache[(s, p)] = True
                return True

            p_left, p_right = p[:q_pos], p[q_pos+1:]
            #print(f"2. '{p_left}', ?, '{p_right}'")
            
            # Split S at all letters (any can be an "?")
            for n in range(len(s)):
                s_left, s_right = s[:n], s[n+1:]
                #print(f"2. ? split:, '{s_left}', ?, '{s_right}'")

                # Next step would be recursive comparison
                if self.isMatch_v1(s_left, p_left) and self.isMatch_v1(s_right, p_right):
                    self.cache[(s, p)] = True
                    return True
            
            self.cache[(s, p)] = False
            return False

        # 3. "*" Pattern

        # At this moment p is either empty or * (or multiple *, which doesn't matter)
        if s=="" and p=="":
            #print('3. s=="" and p=="", True')
            self.cache[(s, p)] = True
            return True
        # * or multiple *s
        elif p=="*" or p!="" and p.count("*") == len(p):
            #print('3. p=="*", True')
            self.cache[(s, p)] = True
            return True
        elif s!="" and p=="":
            #print('3. s!="" and p=="", False')
            self.cache[(s, p)] = False
            return False

        # Should never reach this one
        self.cache[(s, p)] = False
        return False

def main():
    ''' Test isMatch
    '''
    solution = Solution()

    test_cases = [
        ("abb", "*a*b"),
        ("abcd", "a*bc*?"),
        ("aa", "a"),
        ("aa", "aa***"),
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
        result1 = solution.isMatch_v1(s, p)
        elapsed = time.time() - start
        print(s[:50], p[:50], result, elapsed, result==result1, "\n")
        #break

if __name__ == "__main__":
    import time

    main()
