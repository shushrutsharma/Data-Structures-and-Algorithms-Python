# longest substring without repeating characters | leetcode 03 | https://leetcode.com/problems/longest-substring-without-repeating-characters
# sliding window; remove elements until last occurence of current duplicate

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptrL = 0
        seen = dict()
        longest = 0

        for ptrR in range(len(s)):
            while seen.get(s[ptrR]) is not None:
                seen.pop(s[ptrL])
                ptrL += 1
            seen[s[ptrR]] = True
            longest = max(ptrR - ptrL + 1, longest)

        return longest
                 