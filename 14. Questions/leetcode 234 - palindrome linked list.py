# palindrome linked list | leetcode 234 | https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # to check if its palindrome
    def isPalindrome(self, head) -> bool:
        
        # if underflow, is palindrome
        if not head or not head.next: return True
        
        # get one before mid element
        # and check if number of elements are even
        mid, even = self.get_mid(head)
        second = mid.next
        if not even: second = second.next
        
        # reverse the first half of the linked list
        first = self.rev_ll(head, mid)
        
        # match the reversed 1st and normal 2nd halves
        while first and second:
            if first.val != second.val: return False
            first = first.next
            second = second.next
        return True
        

    # to reverse the linked list half
    def rev_ll(self, head, upto):
        prev, curr = None, head
            
        while curr and prev != upto:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
            
    # to get the mid element
    # and check for even
    def get_mid(self, head):
        prev = head
        slow = head
        fast = head.next
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if not fast:    return prev, False
        return slow, True
