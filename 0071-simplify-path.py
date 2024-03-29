''' https://leetcode.com/problems/simplify-path/
'''

class Solution:
    def simplifyPath(self, path):

        good_parts = []
        
        for part in path.split("/"):

            if part in (".", ""):
                continue
            elif part == "..":
                good_parts.pop() if good_parts else None
            else:
                good_parts.append(part)

        return "/" + "/".join(good_parts)


def main():
    ''' Test simplifyPath
    '''
    solution = Solution()

    test_cases = [
        "/"
        "/home/",
        "/../",
        "/home//foo/",
    ]

    for path in test_cases:
        result = solution.simplifyPath(path)
        print(path, result)

if __name__ == "__main__":
    main()
