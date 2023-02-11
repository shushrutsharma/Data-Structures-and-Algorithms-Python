# three sum | leetcode 15 | https://leetcode.com/problems/3sum/
# - sorted; nested loop; outer loop for first element 
# - inner loop for two sum on rest of list
# - avoid duplicates by shifting window till last occurrence

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        N = len(nums)
        triplets = []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            ptrL = i + 1
            ptrR = N - 1
            while ptrL < ptrR:
                s = nums[i] + nums[ptrL] + nums[ptrR]
                if s > 0:
                    ptrR -= 1
                elif s < 0:
                    ptrL += 1
                else:
                    triplets.append([nums[i], nums[ptrL], nums[ptrR]])
                    ptrL += 1
                    while nums[ptrL] == nums[ptrL - 1] and ptrL < ptrR:
                        ptrL += 1
                
        return triplets