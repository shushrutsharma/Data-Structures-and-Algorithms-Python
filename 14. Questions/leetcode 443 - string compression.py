# string compression | leetcode 443 | https://leetcode.com/problems/string-compression/
# sliding window to keep track of a char's occurence

class Solution:
    def compress(self, chars: list[str]) -> int:
        ptrL, ptrR = 0, 0
        total = 0
        chars += " "

        while ptrR < len(chars):
            if chars[ptrL] != chars[ptrR]:
                chars[total] = chars[ptrL]
                total += 1
                group = ptrR - ptrL
                if group > 1:
                    for x in str(group):
                        chars[total] = x
                        total += 1
                ptrL = ptrR
            ptrR += 1
            
        return total
