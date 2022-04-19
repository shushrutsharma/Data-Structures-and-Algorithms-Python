"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Question: https://leetcode.com/problems/length-of-last-word/

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        last = s[len(s)-1]
        return (len(last))