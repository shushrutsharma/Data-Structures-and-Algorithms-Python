# capacity to ship packages within D days | leetcode 1011 | https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# binary search on a range of min and max capacity required 
# min capacity = max(weights) and max capacity = sum(weights)

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = high
        
        # check if days required for a capacity is less than D
        def isPossible (capacity):
            daysReq = 1
            window = capacity
            for weight in weights:
                if window - weight < 0:
                    window = capacity
                    daysReq += 1
                window -= weight

            return daysReq <= days

        # binary search on [min...max]
        while low <= high:
            mid = (high + low) // 2

            if isPossible(mid):
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return res

