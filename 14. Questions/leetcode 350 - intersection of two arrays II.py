"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 
Question: https://leetcode.com/problems/intersection-of-two-arrays-ii/


"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        output=[]
        for n in (nums2):
            if c[n] > 0:
                output.append(n)
                c[n]-=1

        return (output)
