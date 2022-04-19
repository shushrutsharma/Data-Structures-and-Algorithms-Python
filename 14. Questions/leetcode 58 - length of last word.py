"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Question: https://leetcode.com/problems/length-of-last-word/

"""

#Solution usinf inbuilt fuctions : 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        last = s[len(s)-1]
        return (len(last))


#Solution without inbuilt fuctions : 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s)-1, 0
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
            
