# find the town judge | leetcode 997 | https://leetcode.com/problems/find-the-town-judge/submissions/
# method: decrement trust value if you trust someone, increment if someone trusts you

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        # for each person
        # trust += 1 if someone trusts you
        # trust -= 1 if you trust someone
        trustValue = [0] * (n + 1)
        
        for edge in trust:
            trustValue[edge[0]] -= 1
            trustValue[edge[1]] += 1
        
        for i in range(1, n + 1):
            if trustValue[i] == (n - 1):
                return i
        
        return -1
            
