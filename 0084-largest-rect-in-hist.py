''' https://leetcode.com/problems/largest-rectangle-in-histogram/
'''

class Solution:
    def largestRectangleArea(self, heights):

        max_area = max(heights)

        stack = []

        for pos, height in enumerate(heights):

            # First bar, initiate the stack
            if stack == []:
                stack.append((height, pos))
                continue

            # New bar is higher or equal
            if height >= stack[-1][0]:

                # Area is the left (lower) bar * distance + 1
                for h, p in stack[::-1]:
                    max_area = max(max_area, h * (pos - p + 1))
                # The very first column in stack can for rectangle that goes to 0
                max_area = max(max_area, stack[0][0] * (pos + 1))

                # If it is strictly higher, add to stack 
                if height > stack[-1][0]:
                    stack.append((height, pos))

            # New bar is lower
            else:
                # Remove all bars in stack that are higher or equal
                insert_position = pos
                while stack and stack[-1][0] >= height:
                    # Remember last removed bar
                    insert_position = stack.pop()[1]

                # Place new bar in a stack, but record its position as a bar it just replaced
                stack.append((height, insert_position))

                for h, p in stack[::-1]:
                    max_area = max(max_area, h * (pos - p + 1))
                max_area = max(max_area, stack[0][0] * (pos + 1))

        return max_area

    def largestRectangleArea_brute(self, heights):
        # Consider single columns
        max_area = max(heights)

        for start in range(len(heights) - 1):
            for end in range(start + 1, len(heights)):
                width = end - start + 1
                height = min(heights[start:end + 1])
                max_area = max(max_area, width * height)

        return max_area

def random_tests(runs=100):
    solution = Solution()
    for _ in range(runs):
        heights = [random.randint(0, 10) for _ in range(random.randint(1, 10))]
        result = solution.largestRectangleArea(heights)
        result_brute = solution.largestRectangleArea_brute(heights)
        if result != result_brute:
            print(f"Error on: {heights} {result} ({result_brute})")
            break
    else:
        print(f"{runs} tests okay")

def main():
    ''' Test the largestRectangleArea
    '''

    test_cases = [
        [2, 1, 5, 6, 2, 3],
        [2, 4],
        [7, 4, 8, 0, 8, 5],
        ]

    solution = Solution()
    for heights in test_cases:
        result = solution.largestRectangleArea(heights)
        result_brute = solution.largestRectangleArea_brute(heights)
        print(f"{heights} {result} ({result_brute})")


if __name__ == "__main__":
    import random
    main()
    random_tests(10000)
