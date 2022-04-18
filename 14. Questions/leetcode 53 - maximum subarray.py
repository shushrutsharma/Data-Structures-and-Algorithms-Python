"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Question: https://leetcode.com/problems/maximum-subarray/


"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum <0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub