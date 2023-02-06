# longest consecutive sequence | leetcode 128 | https://leetcode.com/problems/longest-consecutive-sequence/
# set to look-up previous and next numbers; nested while loop is O(2n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0

        all = set(nums)
        longest = 0

        for each in all:
            if each - 1 not in all:
                curr = each
                seq = 1
                while curr + 1 in all:
                    seq += 1
                    curr = curr + 1
                if seq > longest:
                    longest = seq

        return longest