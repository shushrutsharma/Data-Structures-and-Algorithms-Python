"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

Question: https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/

"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        a = max(nums)
        for i in range(len(nums)):
            if nums[i] == a:
                b = i
        nums.remove(a)
        count = 0
        for i in nums:
            if (a >= 2*i):
                count = count +1
        if count == len(nums):
            return b
        else:
            return -1