"""
Given two binary strings a and b, return their sum as a binary string.

Question: https://leetcode.com/problems/add-binary/

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        aCount = len(a) - 1
        bCount = len(b) - 1
        
        carry = 0
        
        while aCount >= 0 or bCount >= 0:
            totalSum = carry
            if aCount >= 0:
                totalSum += int(a[aCount])
                aCount -= 1
            if bCount >= 0:
                totalSum += int(b[bCount])
                bCount -= 1
            result = str(totalSum % 2) + result
            carry = totalSum // 2
        if carry > 0:
            result = str(1) + result
        return result