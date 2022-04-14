"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Question: https://leetcode.com/problems/palindrome-number/

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        c = x
        b = 0
        
        while c:
            b = b * 10 + c % 10
            c //= 10
            
        return b == x
        