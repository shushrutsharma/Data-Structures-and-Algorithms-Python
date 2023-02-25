# target sum | leetcode 494 | https://leetcode.com/problems/target-sum/
# 0/1 knapsack to decide +/- and cache (index, total)

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        N = len(nums)
        mem = dict()

        if N == 0:
            return 0

        def knapsack(n, s):
            if n == N:
                return 1 if s == target else 0
            
            if (n, s) in mem:
                return mem[(n, s)]
            
            mem[(n, s)] = knapsack(n+1, s + nums[n]) + knapsack(n+1, s - nums[n])
            return mem[(n, s)]

        return knapsack(0, 0)
