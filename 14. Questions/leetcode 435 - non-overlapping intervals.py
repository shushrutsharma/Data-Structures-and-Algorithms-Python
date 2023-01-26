# non-overlapping intervals | leetcode 435 | https://leetcode.com/problems/non-overlapping-intervals
# sort by starting times; keep track of latest ending time; always keep interval with min end time

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        min_intervals_to_remove = 0
        intervals.sort(key = lambda x: x[0])
        latest_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < latest_end:
                min_intervals_to_remove += 1
                latest_end = min(intervals[i][1], latest_end)
            else:
                latest_end = intervals[i][1]

        return min_intervals_to_remove
