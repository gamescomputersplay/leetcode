''' https://leetcode.com/problems/restore-ip-addresses/
'''

class Solution:
    def restoreIpAddresses(self, s):

        def parse_rec(sofar, s):

            # End recursion of the string is over
            if s == "":
                # If you happen to have 4 numbers - return them
                if len(sofar) == 4:
                    # But make them list of strings first
                    result.append([str(s) for s in sofar])
                return

            p = 1
            while True:

                # Prevent numbers with leading zeros
                if p > 1 and s[0] == "0":
                    break

                # Make the number from the beginning of the string
                n = int(s[:p])
                # but no bigger than 255
                if n > 255:
                    break

                # Recursively try the next number
                new_sofar = sofar.copy()
                new_sofar.append(n)
                parse_rec(new_sofar, s[p:])

                # Try longer number
                p += 1
                if p > len(s):
                    break

        result = []
        # Run recursive algorythm
        parse_rec([], s)
        # Convert to strings
        return [".".join(ip) for ip in result]

def main():
    ''' Test restoreIpAddresses
    '''
    solution = Solution()

    test_cases = [
        "25525511135",
        "0000",
        "1111111111",
        "101023",
    ]
    for s in test_cases:
        result = solution.restoreIpAddresses(s)
        print(f"{s}: {result}")

if __name__ == "__main__":
    main()