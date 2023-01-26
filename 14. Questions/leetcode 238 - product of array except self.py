# product of array except self | leetcode 238 | https://leetcode.com/problems/product-of-array-except-self/
# save prefixes to result array and apply postfix in reverse 
# (since output array doesnt increase space complexity)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        N = len(nums)
        
        # save prefix to result array
        product = 1
        for i in range(N):
            product = nums[i] * product
            result.append(product)

        # update result array as per postfix
        postfix = 1
        for i in range(N - 1, 0, -1):
            result[i] = result[i - 1] * postfix
            postfix = postfix * nums[i]
        result[0] = postfix

        return result
    