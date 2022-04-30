"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Question: https://leetcode.com/problems/merge-sorted-array/

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        
        #merge in reverse order
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m = m-1
            else:
                nums1[last] = nums2[n-1]
                n = n-1
            last = last - 1
            
        #fill nums1 with leftover nums2 elements
        while n>0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last -1