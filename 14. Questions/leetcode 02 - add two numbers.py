# add two numbers | leetcode 02 | https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:
        res = ListNode()
        head = res

        while l1 != None or l2 != None:
            if l1 == None:
                this_val = res.val + l2.val
                l2 = l2.next
            elif l2 == None:
                this_val = res.val + l1.val
                l1 = l1.next
            else:                
                this_val = res.val + l1.val + l2.val
                l1, l2 = l1.next, l2.next

            this_digit = this_val % 10
            next_digit = this_val // 10

            res.val = this_digit
            if l1 != None or l2 != None:
                res.next = ListNode(next_digit)
                res = res.next
                
        if next_digit > 0:
            res.next = ListNode(next_digit)
            res = res.next

        return head
        