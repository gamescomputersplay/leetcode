''' https://leetcode.com/problems/maximum-product-subarray/
'''

class Solution:
    def maxProduct(self, nums):

        def max_product_non_zero(nums):
            ''' Calculate MaxProduct, give nums don't contain zeros
            '''

            # In case there is only one element: it is a product
            if len(nums) == 1:
                return nums[0]
            
            # Product of all elements
            product = 1
            for num in nums:
                product *= num
            
            # If it is already positive - it's the answer
            if product > 0:
                return product
            
            # Otherwise calculate how much product it would take
            # to get to a negative number from left and right

            left = 1
            for num in nums:
                left *= num
                if left < 0:
                    break

            right = 1
            for num in nums[::-1]:
                right *= num
                if right < 0:
                    break

            return max(product // left, product // right)

        start = None
        max_product = max(nums)

        # Break into non-zero chunks, calculate max for each chunk
        for curr_pos, num in enumerate(nums + [0]):
            if num != 0 and start is None:
                start = curr_pos
            elif num == 0 and start != None:
                local_max = max_product_non_zero(nums[start:curr_pos])
                max_product = max(max_product, local_max)
                start = None

        return max_product

def main():
    ''' Test maxProduct
    '''
    solution = Solution()

    test_cases = [
        [2,3,-2,4], #6
        [-2,0,-1], #0
        [1, -2, 3, 4, 0, -5, 6, -7, 0, 9, 10, -11],
        [-1],
    ]
    for nums in test_cases:
        result = solution.maxProduct(nums)
        print(f"{nums}: {result}")


if __name__ == "__main__":
    main()
        