# naming a company | leetcode 2306 | https://leetcode.com/problems/naming-a-company
# bucket by starting character to make it n(26^2.n) and compare each set with each other

class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        buckets = dict()
        num_distinct = 0

        for idea in ideas:
            if buckets.get(idea[0]) is None:
                buckets[idea[0]] = {idea[1:]}
            else:
                buckets[idea[0]].add(idea[1:])

        for prefix_i, suffix_i in buckets.items():
            for prefix_j, suffix_j in buckets.items():
                if prefix_i == prefix_j:
                    continue
                common = len(suffix_i & suffix_j)
                common_i = len(suffix_i) - common
                common_j = len(suffix_j) - common
                num_distinct += common_i * common_j
        
        return num_distinct