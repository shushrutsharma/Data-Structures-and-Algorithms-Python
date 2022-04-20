"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Question: https://leetcode.com/problems/plus-one/

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in range(len(digits)):
            n = (n*10)+digits[i]
        n = n+1
        m = map(int, str(n))
        return(m)
        