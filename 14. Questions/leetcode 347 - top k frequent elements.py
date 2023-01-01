# top k frequency elements | leetcode 347 | https://leetcode.com/problems/top-k-frequent-elements/
# use buckets with each bucket being the frequency of an element

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        N = len(nums)

        # create buckets where index = frequency of element
        buckets = [[] for x in range(N + 1)]
        for f in freq:
            buckets[freq[f]].append(f)

        # get k elements starting from the end of the bucket
        k_mf = []
        for x in buckets[::-1]:
            if k > 0:
                if x != []:
                    k_mf += x
                    k -= len(x)
            else:
                return k_mf
                