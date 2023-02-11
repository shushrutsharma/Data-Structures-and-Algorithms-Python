# two sum II - input array is sorted | leetcode 167 | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# use two pointers on sorted array; if sum > target slide window left, else slide window right

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ptrL = 0
        ptrR = 1
        N = len(numbers)

        while ptrR < N:
            s = numbers[ptrR] + numbers[ptrL]
            if s == target:
                return [ptrL + 1, ptrR + 1]
            elif s < target:
                ptrL += 1
                ptrR += 1
            else:
                ptrL -= 1
            
        # unreachable for testcases with exactly one solution
        return [-1, -1]