# find the index of the first occurrence of a string | leetcode 28 | https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# sliding window to match each character of the haystack with the needle; no slices.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # ----- using regex -----
        # if needle == '':
        #     return 0
        
        # import re
        # match = re.search(needle, haystack)
        # return match.start() if match else -1

        # ----- using sliding windows -----
        ptrL, ptrR = 0, 0
        N_needle, N_haystack = len(needle), len(haystack)
        while ptrR < N_haystack:
            if haystack[ptrR] == needle[ptrR - ptrL]:
                ptrR += 1
                if ptrR - ptrL > N_needle - 1:
                    return ptrL
            else:
                ptrR = ptrL + 1
                ptrL += 1
        
        return -1
