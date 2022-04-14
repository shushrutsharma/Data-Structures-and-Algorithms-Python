"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Questions: https://leetcode.com/problems/longest-common-prefix/

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        n = len(strs)
        strs.sort()
        first = strs[0]
        last = strs[n-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return res
            else:
                res = res + first[i]
        return res
        
        
        
#         for i in range(len(strs[0])):
#             for s in strs:
#                 if i == len(s) or s[i] != strs[0][i]:
#                     return res
                
#             res += strs[0][i]
            
#         return res