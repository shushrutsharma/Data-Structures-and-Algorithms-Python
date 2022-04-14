"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Question: https://leetcode.com/problems/valid-parentheses/


"""


class Solution:
    def isValid(self, s: str) -> bool:
        para = {')':'(', ']':'[', '}':'{'}
        op = ['(','[', '{']
        stack = []
        
        for c in s:
            if c in op:
                stack.append(c)
            
            elif c in para:
                if len(stack) != 0 and stack[-1] == para[c]:
                    stack.pop()
                else:
                    return False
                    
        if len(stack) == 0:
            return True
        else:
            return False
            
            
            
            
            
            
#             if c in para:
#                 if len(stack) != 0 and stack[-1] == para[c]:
#                     stack.pop()
#                 else:
#                     return False
                
#             else:
#                 stack.append(c)
                
#         if len(stack) == 0:
#             return True
#         else:
#             False