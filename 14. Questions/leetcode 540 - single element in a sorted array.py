# single element in a sorted array | leetcode 540 | https://leetcode.com/problems/single-element-in-a-sorted-array/
# binary search over sorted array; check if mid is even and mid is the first of the duplicates

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        N = len(nums)
        if N < 2:
            return nums[0]
        low, high, mid = 0, N, 0
        while low <= high:
            mid = low + ((high - low) // 2)

            if mid == N - 1:
                return nums[mid]

            if nums[mid] == nums[mid - 1] or nums[mid] == nums[mid + 1]:
                if (mid % 2 == 0) == (nums[mid] == nums[mid + 1]):
                    low = mid
                else:
                    high = mid
            else:
                return nums[mid]
        
        return nums[mid]