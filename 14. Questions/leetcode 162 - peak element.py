# find peak element | leetcode 162 | https://leetcode.com/problems/find-peak-element/
# using binary search to determine 
# if the "middle" element is on a +ve / -ve slope

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        a = 0
        b = len(nums) - 1
        while a < b:
            k = (a + b) // 2
            if nums[k] > nums[k + 1]:
                b = k
            else:
                a = k + 1
                
        return a