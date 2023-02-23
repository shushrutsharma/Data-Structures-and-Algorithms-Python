# IPO | leetcode 502 | https://leetcode.com/problems/ipo/
# min-heap to track capital and max-heap to track profits

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        maxHeap = []
        minHeap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minHeap)

        for _ in range(k):
            while minHeap and minHeap[0][0] <= w:
                _, p = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -1 * p)
            if not maxHeap:
                break
            w += -1 * heapq.heappop(maxHeap)

        return w

